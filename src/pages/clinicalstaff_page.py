from tkinter import *
from tkinter import ttk
from .base_page import Page
from services.clinical_staff_service import Clinical_Staff_Service


class Clinical_Staff_Page(Page):

    def __init__(self, parent, *args, **kwargs):
        Page.__init__(self, parent, *args, **kwargs)

        # Creando el contenedor Frame
        frame = LabelFrame(self, text="Registrar nuevo personal clinico")
        frame.grid(row=0, column=0, columnspan=7, pady=20)

        # Campos de entrada para Nombre, Apellido, Cédula, Teléfono, Dirección y cargo
        Label(frame, text="Nombre: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        Label(frame, text="Apellido: ").grid(row=1, column=2)
        self.last_name = Entry(frame)
        self.last_name.grid(row=1, column=3)

        Label(frame, text="Cédula: ").grid(row=2, column=0)
        self.cedula = Entry(frame)
        self.cedula.grid(row=2, column=1)

        Label(frame, text="Teléfono: ").grid(row=2, column=2)
        self.phone = Entry(frame)
        self.phone.grid(row=2, column=3)

        Label(frame, text="Dirección: ").grid(row=3, column=0)
        self.address = Entry(frame)
        self.address.grid(row=3, column=1)

        Label(frame, text="Cargo: ").grid(row=3, column=2)
        self.cargo = Entry(frame)
        self.cargo.grid(row=3, column=3)

        # Botón para guardar personal
        ttk.Button(frame, text="Guardar trabajador", command=self.add_clinical_staff).grid(
            row=4, columnspan=4, sticky=W + E
        )

        # Mensaje de salida
        self.message = Label(self, text="", fg="blue")
        self.message.grid(row=1, column=0, columnspan=2, sticky=W + E)

        # Tabla para mostrar personal
        self.tree = ttk.Treeview(self, height=10, columns=(1, 2, 3, 4, 5))
        self.tree.grid(row=2, column=0, columnspan=4)
        self.tree.heading("#0", text="Nombre", anchor=CENTER)
        self.tree.heading("#1", text="Apellido", anchor=CENTER)
        self.tree.heading("#2", text="Cédula", anchor=CENTER)
        self.tree.heading("#3", text="Teléfono", anchor=CENTER)
        self.tree.heading("#4", text="Dirección", anchor=CENTER)
        self.tree.heading("#5", text="Cargo", anchor=CENTER)

        # Botones adicionales
        ttk.Button(self, text="ELIMINAR", command=self.delete_clinical_staff).grid(
            row=3, column=0, sticky=W + E
        )
        ttk.Button(self, text="EDITAR", command=self.edit_clinical_staff).grid(
            row=3, column=1, sticky=W + E
        )

        # Rellenar las filas con personal existentes
        self.get_clinical_staff()

    def get_clinical_staff(self):
        # Limpiar la tabla de personal
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        # Obtener el personal desde el servicio
        result = Clinical_Staff_Service.get_clinical_staff()

        # Insertar cada personal en la tabla
        for row in result:
            self.tree.insert("", 0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))

    def validation(self):
        return (
            len(self.name.get()) != 0
            and len(self.last_name.get()) != 0
            and len(self.cedula.get()) != 0
            and len(self.phone.get()) != 0
            and len(self.address.get()) != 0
            and len(self.cargo.get()) != 0
        )

    def add_clinical_staff(self):
        if self.validation():
            # Llamar al método estático add_clinical_staff de Clinical_Staff_Service
            response_data = Clinical_Staff_Service.add_clinical_staff(
                parameters=(
                    self.name.get(),
                    self.last_name.get(),
                    self.cedula.get(),
                    self.phone.get(),
                    self.address.get(),
                    self.cargo.get(),
                )
            )
            # Mostrar mensaje de éxito o error
            self.message["text"] = response_data

            # Limpiar los campos de entrada
            self.name.delete(0, END)
            self.last_name.delete(0, END)
            self.cedula.delete(0, END)
            self.phone.delete(0, END)
            self.address.delete(0, END)
            self.cargo.delete(0, END)

            # Actualizar la tabla de personal
            self.get_clinical_staff()
        else:
            self.message["text"] = "Todos los campos son requeridos"

    def delete_clinical_staff(self):
        # Obtener el nombre del personal seleccionado en la tabla
        selected_item = self.tree.selection()
        if not selected_item:
            self.message["text"] = "Por favor seleccione un registro"
            return

        # Obtener el nombre del personal seleccionado
        name = self.tree.item(selected_item)["text"]

        # Llamar al método estático delete_clinical_staff de Clinical_Staff_Service
        response_data = Clinical_Staff_Service.delete_clinical_staff(parameters=(name,))
        self.message["text"] = response_data

        # Actualizar la tabla del personal
        self.get_clinical_staff()

    def edit_clinical_staff(self):
        # Obtener el trabajador seleccionado en la tabla
        selected_item = self.tree.selection()
        if not selected_item:
            self.message["text"] = "Por favor, seleccione un registro"
            return

        # Obtener los datos del trabajador seleccionado
        name = self.tree.item(selected_item)["text"]
        old_last_name = self.tree.item(selected_item)["values"][0]
        old_cedula = self.tree.item(selected_item)["values"][1]
        old_phone = self.tree.item(selected_item)["values"][2]
        old_address = self.tree.item(selected_item)["values"][3]
        old_cargo = self.tree.item(selected_item)["values"][4]

        # Crear una ventana emergente para editar el trabajador
        self.edit_wind = Toplevel()
        self.edit_wind.title("Editar Paciente")

        # Campos de entrada para editar el trabajador
        Label(self.edit_wind, text="Nuevo nombre:").grid(row=1, column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1, column=2)
        new_name.insert(0, name)

        Label(self.edit_wind, text="Nuevo apellido:").grid(row=2, column=1)
        new_last_name = Entry(self.edit_wind)
        new_last_name.grid(row=2, column=2)
        new_last_name.insert(0, old_last_name)

        Label(self.edit_wind, text="Nueva cédula:").grid(row=3, column=1)
        new_cedula = Entry(self.edit_wind)
        new_cedula.grid(row=3, column=2)
        new_cedula.insert(0, old_cedula)

        Label(self.edit_wind, text="Nuevo teléfono:").grid(row=4, column=1)
        new_phone = Entry(self.edit_wind)
        new_phone.grid(row=4, column=2)
        new_phone.insert(0, old_phone)

        Label(self.edit_wind, text="Nueva dirección:").grid(row=5, column=1)
        new_address = Entry(self.edit_wind)
        new_address.grid(row=5, column=2)
        new_address.insert(0, old_address)

        Label(self.edit_wind, text="Nuevo cargo:").grid(row=6, column=1)
        new_cargo = Entry(self.edit_wind)
        new_cargo.grid(row=6, column=2)
        new_cargo.insert(0, old_cargo)

        # Botón para actualizar los datos del trabajador
        Button(
            self.edit_wind,
            text="Actualizar",
            command=lambda: self.edit_records(
                name,
                new_name.get(),
                new_last_name.get(),
                new_cedula.get(),
                new_phone.get(),
                new_address.get(),
                new_cargo.get(),
                old_last_name,
                old_cedula,
                old_phone,
                old_address,
                old_cargo,
            ),
        ).grid(row=7, column=2, sticky=W)

    def edit_records(
        self,
        name,
        new_name,
        new_last_name,
        new_cedula,
        new_phone,
        new_address,
        new_cargo,
        old_last_name,
        old_cedula,
        old_phone,
        old_address,
        old_cargo,
    ):
        # Llamar al método estático edit_clinical_staff de Clinical_Staff_Service
        response_data = Clinical_Staff_Service.edit_clinical_staff(
            parameters=(
                new_name,
                new_last_name,
                new_cedula,
                new_phone,
                new_address,
                new_cargo,
                name,
                old_last_name,
                old_cedula,
                old_phone,
                old_address,
                old_cargo,
            )
        )
        self.edit_wind.destroy()  # Cerrar la ventana de edición
        self.message["text"] = response_data  # Mostrar mensaje de éxito o error
        self.get_patients()  # Actualizar la tabla de pacientes

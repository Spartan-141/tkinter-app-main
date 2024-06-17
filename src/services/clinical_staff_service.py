from utils.run_query import run_query

class Clinical_Staff_Service:
    @staticmethod
    def get_clinical_staff():
        query = "SELECT * FROM clinicalstaff ORDER BY nombre DESC"
        result = run_query(query)
        return result

    @staticmethod
    def add_clinical_staff(parameters):
        query = "INSERT INTO clinicalstaff VALUES(NULL, ?, ?, ?, ?, ?, ?)"
        run_query(query, parameters)
        return "Trabajador agregado exitosamente"

    @staticmethod
    def delete_clinical_staff(parameters):
        query = "DELETE FROM clinicalstaff WHERE nombre = ?"
        run_query(query, parameters)
        return "Registro eliminado exitosamente"

    @staticmethod
    def edit_clinical_staff(parameters):
        query = """
            UPDATE clinicalstaff 
            SET nombre = ?, apellido = ?, cedula = ?, telefono = ?, direccion = ?, cargo = ? 
            WHERE nombre = ? AND apellido = ? AND cedula = ? AND telefono = ? AND direccion = ? AND cargo = ?
        """
        run_query(query, parameters)
        return "Registro actualizado correctamente"
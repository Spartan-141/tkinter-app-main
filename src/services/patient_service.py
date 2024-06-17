from utils.run_query import run_query

class PatientService:
    @staticmethod
    def get_patients():
        query = "SELECT * FROM paciente ORDER BY nombre DESC"
        result = run_query(query)
        return result

    @staticmethod
    def add_patient(parameters):
        query = "INSERT INTO paciente VALUES(NULL, ?, ?, ?, ?, ?, ?)"
        run_query(query, parameters)
        return "Paciente agregado exitosamente"

    @staticmethod
    def delete_patient(parameters):
        query = "DELETE FROM paciente WHERE nombre = ?"
        run_query(query, parameters)
        return "Registro eliminado exitosamente"

    @staticmethod
    def edit_patient(parameters):
        query = """
            UPDATE paciente 
            SET nombre = ?, apellido = ?, cedula = ?, telefono = ?, direccion = ?, diagnostico = ? 
            WHERE nombre = ? AND apellido = ? AND cedula = ? AND telefono = ? AND direccion = ? AND diagnostico = ?
        """
        run_query(query, parameters)
        return "Registro actualizado correctamente"


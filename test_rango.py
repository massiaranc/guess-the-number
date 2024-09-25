import unittest
from unittest.mock import patch
from main import intento_usuario
from main import juego


class TestIngresosUsuario(unittest.TestCase):

    @patch('builtins.input', side_effect=['-12', '50'])  # Simular que primero ingresa un número negativo y luego uno válido
    @patch('builtins.print')  # Simular la función print
    def test_ingreso_valido_negativo(self, mock_print, mock_input):
        historial = []
        intento_usuario(historial)
        
        # Verificar que se imprime el mensaje de error para un número negativo
        mock_print.assert_called_with("Error, el número debe estar entre 1 y 100.")

    @patch('builtins.input', side_effect=['150', '60'])  # Simular que primero ingresa un número fuera de rango
    @patch('builtins.print')  # Simular la función print
    def test_ingreso_valido_fuera_de_rango(self, mock_print, mock_input):
        historial = []
        intento_usuario(historial)

        # Verificar que se imprime el mensaje de error para un número fuera de rango
        mock_print.assert_called_with("Error, el número debe estar entre 1 y 100.")

    @patch('builtins.input', side_effect=['abc', '50'])  # Simular que primero ingresa letras y luego un número válido
    @patch('builtins.print')  # Simular la función print
    def test_ingreso_letras(self, mock_print, mock_input):
        historial = []
        intento_usuario(historial)
        
        # Verificar que se imprime el mensaje de error para entrada no numérica
        mock_print.assert_called_with("Entrada no válida. Por favor, ingresa un número entero.")

    @patch('builtins.input', side_effect=['@#$', '70'])  # Simular que primero ingresa caracteres especiales y luego un número válido
    @patch('builtins.print')  # Simular la función print
    def test_ingreso_caracteres_especiales(self, mock_print, mock_input):
        historial = []
        intento_usuario(historial)

        # Verificar que se imprime el mensaje de error para caracteres especiales
        mock_print.assert_called_with("Entrada no válida. Por favor, ingresa un número entero.")

class TestAciertoUsuario(unittest.TestCase):

    @patch('builtins.print')  # Simular la función print
    @patch('main.intento_usuario', return_value=42)  # Simular que el usuario ingresa 42
    @patch('main.obtener_nombre_usuario', return_value="Juan")  # Simular el nombre del usuario
    @patch('main.generar_numero_secreto', return_value=42)  # Simular que el número secreto es 42
    def test_acierto_numero_secreto(self, mock_generar_numero, mock_nombre, mock_intento_usuario, mock_print):
        historial_intentos = []  # Simular el historial de intentos

        # Llamar a la función juego(), donde el número secreto será el que hemos simulado
        juego()

        # Verificar que se imprime el mensaje de felicitaciones con el nombre del usuario
        mock_print.assert_any_call("¡Felicidades Juan ! Adivinaste el número secreto. ")



if __name__ == '__main__':
    unittest.main()
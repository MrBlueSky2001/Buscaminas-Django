from django import forms

def validador_filas_columnas(value, filas_min=0, filas_max=20, columnas_min=0, columnas_max=15):
    if value < filas_min or value > filas_max:
        raise forms.ValidationError(f"El valor debe estar entre {filas_min} y {filas_max} para filas.")
    if value < columnas_min or value > columnas_max:
        raise forms.ValidationError(f"El valor debe estar entre {columnas_min} y {columnas_max} para columnas.")

class TableroForm(forms.Form):
    filas = forms.IntegerField(validators=[validador_filas_columnas])
    columnas = forms.IntegerField(validators=[validador_filas_columnas])
    num_minas = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        filas = cleaned_data.get('filas')
        columnas = cleaned_data.get('columnas')
        num_minas = cleaned_data.get('num_minas')

        if num_minas:
            if num_minas < 0:
                self.add_error('num_minas', 'El número de minas debe ser mayor o igual a 0.')

            if num_minas > (filas * columnas) / 2:
                self.add_error('num_minas', 'El número de minas debe ser menor o igual a la mitad de las casillas del tablero.')

        return cleaned_data

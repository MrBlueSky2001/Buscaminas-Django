from django import forms

def validador_filas_columnas(value, filas_min=0, filas_max=20, columnas_min=0, columnas_max=15):
    if value < filas_min or value > filas_max:
        raise forms.ValidationError(f"El valor debe estar entre {filas_min} y {filas_max} para filas.")
    if value < columnas_min or value > columnas_max:
        raise forms.ValidationError(f"El valor debe estar entre {columnas_min} y {columnas_max} para columnas.")

class TableroForm(forms.Form):
    filas = forms.IntegerField(validators=[validador_filas_columnas])
    columnas = forms.IntegerField(validators=[validador_filas_columnas])
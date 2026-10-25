# Carpeta de Datos y Metadatos

En este directorio se almacenan únicamente los archivos de registro tabular y metadatos de trazabilidad en formato CSV.

## Enlaces a almacenamiento externo (Google Drive)
- **Dataset de imágenes limpias (CMP Facades curadas):** [Enlace a Google Drive - Imágenes limpias](https://drive.google.com/drive/folders/1Z_tiElmaImf6PYX3u28YjmG9BZkLplM7)
- **Dataset de imágenes sintéticas generadas (1380 pares):** [Enlace a Google Drive - Imágenes generadas](https://drive.google.com/drive/folders/1LlGhfYI6dwU1Wz-Vat62Rd4HzAhf99E7)
- **Relevamiento manual de degradaciones de Luján (Google Sheets en vivo):** [Planilla Google Sheets](https://docs.google.com/spreadsheets/d/18ubhmg7HilYiEqRyZwZGl_gkyqMUglM07fQ1fdlKwRc/edit?gid=1203896242#gid=1203896242)

## Archivos locales en el repositorio
- `registro_degradaciones_sinteticas.csv`: Registro de las 12 degradaciones aplicadas a cada fachada limpia.
- `relevamiento_lujan_matriz.csv`: Exportación estática del relevamiento para ejecución de scripts en clúster.
- `split_trazabilidad_80_10_10.csv`: Asignación fija de cada fachada a train/val/test.

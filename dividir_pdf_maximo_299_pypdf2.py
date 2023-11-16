import PyPDF2

def dividir_pdf(ruta_archivo):
    pdf = PyPDF2.PdfReader(ruta_archivo)
    total_paginas = len(pdf.pages)
    paginas_por_parte = 100

    # Calcular el número total de partes
    num_partes = total_paginas // paginas_por_parte
    if total_paginas % paginas_por_parte != 0:
        num_partes += 1

    # Dividir el PDF en partes
    for i in range(num_partes):
        inicio = i * paginas_por_parte
        fin = min((i + 1) * paginas_por_parte, total_paginas)
        salida = f"parte{i+1}.pdf"

        # Crear un nuevo PDF con las páginas correspondientes
        pdf_parte = PyPDF2.PdfWriter()
        for pagina in range(inicio, fin):
            pdf_parte.add_page(pdf.pages[pagina])

        # Guardar la parte del PDF en un archivo
        with open(salida, "wb") as f:
            pdf_parte.write(f)

        print(f"Parte {i+1} creada: {salida}")

# Ejemplo de uso
ruta_archivo_pdf = "archivo.pdf"
dividir_pdf(ruta_archivo_pdf)
# python dividir_pdf_maximo_299_pypdf2.py
# alt t s s 

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("""
    <html>
        <body>
            <h1>HELLO</h1>
            <h2>This is HTML format</h2>
        </body>
    </html>
    """)

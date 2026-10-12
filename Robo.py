
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from datetime import datetime

def pesquisar_site(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    dominio = urlparse(url).hostname
    if not dominio:
        print("Endereço inválido.")
        return

    try:
        pedido = Request(
            url,
            headers={"User-Agent": "RoboPesquisa/1.0"}
        )
        with urlopen(pedido, timeout=10) as resposta:
            print("\n--- RESULTADO ---")
            print("Site:", url)
            print("Domínio:", dominio)
            print("Status HTTP:", resposta.status)
            print("Data:", datetime.now().strftime("%d/%m/%Y %H:%M"))
            print("Tipo:", resposta.headers.get("Content-Type"))
    except Exception as erro:
        print("Não foi possível acessar:", erro)

if __name__ == "__main__":
    site = input("Digite o endereço de um site público: ")
    pesquisar_site(site)

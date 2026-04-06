from pick import pick
import sys

def main():
    title = '--- MENU DE OPÇÕES (Use as setas e Enter) ---'
    options = [
        'Iniciar Processo', 
        'Configurações', 
        'Ver Status', 
        'Sair'
    ]

    # A função pick retorna uma tupla (escolha, índice)
    option, index = pick(options, title, indicator='=>', default_index=0)

    if option == 'Sair':
        print("Saindo do programa...")
        sys.exit()
    
    print(f"Você selecionou: {option} (Opção nº {index + 1})")
    input("\nPressione Enter para fechar...")

if __name__ == "__main__":
    main()

# pyinstaller --onefile main.py
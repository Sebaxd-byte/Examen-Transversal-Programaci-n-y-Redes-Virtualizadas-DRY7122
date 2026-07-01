
"""
Asignatura: Programación y Redes Virtualizadas (DRY7122)
Script: validador_asn.py
Objetivo: Validar si un número de AS de BGP es Público o Privado.
Integrantes: Sebastián Arcos y Jorge Manzo
"""

def verificar_asn():
    print("\n" + "="*50)
    print("  VALIDADOR DE SISTEMAS AUTÓNOMOS (ASN) BGP")
    print("="*50)
    
    try:
        asn = int(input("Ingrese el número de AS de BGP a evaluar: "))
        
	 if (64512 <= asn <= 65534) or (4200000000 <= asn <= 4294967295):
            print(f"\n[RESULTADO] El ASN {asn} corresponde a un AS **PRIVADO**.")
        
        
        elif asn == 0 or asn == 65535 or asn == 4294967295:
            print(f"\n[RESULTADO] El ASN {asn} corresponde a un rango **RESERVADO / ESPECIAL**.")
        
        
        elif (1 <= asn <= 64511) or (65536 <= asn <= 4199999999):
            print(f"\n[RESULTADO] El ASN {asn} corresponde a un AS **PÚBLICO**.")
            
        else:
            print(f"\n[ERROR] El número {asn} está fuera de los límites de la arquitectura BGP.")
            
    except ValueError:
        print("\n[ERROR CRÍTICO] Entrada inválida. Ingrese únicamente valores enteros.")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    verificar_asn()

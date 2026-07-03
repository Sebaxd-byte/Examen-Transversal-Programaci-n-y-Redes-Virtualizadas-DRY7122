"""
Asignatura: Programación y Redes Virtualizadas (DRY7122)
Script: netconf_provision.py
Objetivo: Modificar Hostname con apellidos de integrantes e instanciar Loopback 111 vía NETCONF.
Integrantes: Sebastián Arcos y Jorge Manzo
"""

from ncclient import manager
import xml.dom.minidom

def ejecutar_aprovisionamiento_netconf():
    # 1. Definir parámetros de conexión al router CSR1000v (Puerto NETCONF 830)
    router_target = {
        "host": "192.168.56.101",
        "port": 830,
        "username": "cisco",
        "password": "cisco123!",  # Reemplazar con tus credenciales si cambian
        "hostkey_verify": False
    }
    
    # 2. Configurar el Payload XML declarativo usando modelos YANG nativos de Cisco IOS-XE
    # - Cambia el hostname a "Arcos_Manzo"
    # - Crea la interfaz Loopback 111 con la IPv4 111.111.111.111/32
    xml_payload = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <hostname>Arcos_Manzo</hostname>
            <interface>
                <Loopback>
                    <name>111</name>
                    <description>Interfaz Aprovisionada via NETCONF - Examen Transversal</description>
                    <ip>
                        <address>
                            <primary>
                                <address>111.111.111.111</address>
                                <mask>255.255.255.255</mask>
                            </primary>
                        </address>
                    </ip>
                </Loopback>
            </interface>
        </native>
    </config>
    """
    
    print("\n" + "="*60)
    print("[INFO] Estableciendo conexión SSH sobre puerto 830 via NETCONF...")
    print("="*60)
    
    try:
        # Iniciar sesión segura context-managed
        with manager.connect(**router_target) as m:
            print("[SUCCESS] Conexión establecida. Inyectando payload XML de configuración...")
            
            # Realizar llamada API remota (edit-config) apuntando a la running-configuration
            rpc_response = m.edit_config(target="running", config=xml_payload)
            
            print("\n[INFO] Respuesta RPC recibida desde el Router CSR1000v:")
            # Formatear la salida XML limpia para el informe
            xml_limpio = xml.dom.minidom.parseString(rpc_response.xml)
            print(xml_limpio.toprettyxml(indent="  "))
            
    except Exception as e:
        print(f"\n[ERROR CRÍTICO] Fallo en la comunicación con el subsistema NETCONF: {e}")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    ejecutar_aprovisionamiento_netconf()

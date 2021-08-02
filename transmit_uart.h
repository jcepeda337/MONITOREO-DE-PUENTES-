#if !defined(transmit_uart_h)
#define transmit_uart_h 
void transmitir_ascii_datos(char uart_tx_datos);
void transmitir_ascii_comandos(char uart_tx_datos);
void transmitir_datos(char uart_control_datos);
void transmitir_comandos(char uart_control_comandos);
#endif	
# Documentación de Vision Assistant Pro

**Vision Assistant Pro** es un asistente de IA avanzado y multimodal para NVDA. Utiliza motores de IA de primer nivel para proporcionar lectura de pantalla inteligente, traducción, dictado por voz y análisis de documentos.

_Este complemento fue lanzado a la comunidad en honor al Día Internacional de las Personas con Discapacidad._

## 1. Configuración

Ve a **Menú de NVDA > Preferencias > Configuración > Vision Assistant Pro**.

### 1.1 Configuración de conexión
- **Proveedor:** Selecciona tu servicio de IA preferido. Los proveedores compatibles incluyen **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** y **Personalizado** (servidores compatibles con OpenAI como Ollama, LM Studio, Jan.ai o KoboldCPP).
- **Nota importante:** Recomendamos encarecidamente usar **Google Gemini** para obtener el mejor rendimiento y precisión (especialmente para análisis de imágenes/archivos).
- **Clave API:** Obligatorio. Puedes ingresar varias claves (separadas por comas o saltos de línea) para rotación automática.
- **Obtener modelos:** Después de ingresar tu clave API, presiona este botón para descargar la lista más reciente de modelos disponibles del proveedor.
- **Modelo de IA:** Selecciona el modelo principal utilizado para el chat general y análisis.

### 1.2 Enrutamiento avanzado de modelos
*Disponible para todos los proveedores, incluidos Gemini, OpenAI, Groq, Mistral y Personalizado.*

> **⚠️ Advertencia:** Estos ajustes están destinados **solo a usuarios avanzados**. Si no sabes qué hace un modelo específico, déjalo **desmarcado**. Seleccionar un modelo incompatible para una tarea (por ejemplo, un modelo solo de texto para Visión) causará errores y detendrá el funcionamiento del complemento.

Marca **"Enrutamiento avanzado de modelos (específico por tarea)"** para desbloquear el control detallado. Esto te permite seleccionar modelos específicos de la lista desplegable para diferentes tareas:
- **Modelo de OCR/Visión:** Elige un modelo especializado para analizar imágenes.
- **Texto a voz (STT):** Elige un modelo específico para dictado.
- **Voz a texto (TTS):** Elige un modelo para generar audio.
- **Modelo del Operador de IA:** Selecciona un modelo específico para tareas de operación autónoma del equipo.
*Nota: Las funciones no compatibles (por ejemplo, TTS para Groq) se ocultarán automáticamente.*

### 1.3 Configuración avanzada de punto de acceso (Proveedor personalizado)
*Disponible solo cuando se selecciona "Personalizado".*

> **⚠️ Advertencia:** Esta sección permite la configuración manual de la API y está diseñada para **usuarios avanzados** que ejecutan servidores locales o proxies. URLs o nombres de modelos incorrectos interrumpirán la conectividad. Si no sabes exactamente qué son estos puntos de acceso, mantén esto **desmarcado**.

Marca **"Configuración avanzada de punto de acceso"** para ingresar manualmente los detalles del servidor. A diferencia de los proveedores nativos, aquí debes **escribir** las URLs específicas y los nombres de los modelos:
- **URL de lista de modelos:** El punto de acceso para obtener los modelos disponibles.
- **URL de punto de acceso OCR/STT/TTS:** URLs completas para servicios específicos (por ejemplo, `http://localhost:11434/v1/audio/speech`).
- **Modelos personalizados:** Escribe manualmente el nombre del modelo (por ejemplo, `llama3:8b`) para cada tarea.

### 1.3.1 Configurar IA local (Configuración en un paso)
Para hacer la integración con IA local completamente sin conexión extremadamente sencilla, hay un botón dedicado **"Configurar IA local"** disponible dentro de la Configuración del proveedor personalizado.

Si tienes un servidor de modelos de IA local en ejecución en tu equipo:
1. Selecciona **Personalizado** como tu proveedor.
2. Presiona el botón **Configurar IA local**.
3. Elige tu motor de IA local desde el diálogo accesible:
   - **Ollama** (por defecto en `http://127.0.0.1:11434`)
   - **LM Studio** (por defecto en `http://127.0.0.1:1234`)
   - **Jan.ai** (por defecto en `http://127.0.0.1:1337`)
   - **KoboldCPP** (por defecto en `http://127.0.0.1:5001`)
4. El complemento configurará instantáneamente la URL local correcta, el tipo de API, y obtendrá automáticamente tus modelos sin conexión activos para llenar el cuadro de selección del **Modelo de IA**.

*Nota sobre red y proxies:* Este motor de conexión local cuenta con un mecanismo avanzado de omisión de proxy. Incluso si tienes una VPN activa o un proxy en modo TUN, tus solicitudes de IA local lo omitirán completamente, garantizando conexiones sin conexión estables sin errores 502 Bad Gateway.

### 1.4 Preferencias generales
- **Motor OCR:** Elige entre **Chrome (Rápido)** para resultados rápidos o **IA (Avanzado)** para una mejor conservación del diseño.
    - *Nota:* Si seleccionas "IA (Avanzado)" pero tu proveedor es OpenAI/Groq, el complemento enrutará inteligentemente la imagen a tu modelo de visión del proveedor activo.
- **Voz TTS:** Selecciona el estilo de voz que prefieras. Esta lista se actualiza dinámicamente según tu proveedor activo.
- **Creatividad (Temperatura):** Controla la aleatoriedad de la IA. Los valores más bajos son mejores para traducciones/OCR precisas.
- **URL del proxy:** Configura esto si los servicios de IA están restringidos en tu región (admite proxies locales como `127.0.0.1` o URLs puente).

## 2. Capa de comandos y atajos

Para evitar conflictos de teclado, este complemento usa una **Capa de comandos**.
1. Presiona **NVDA + Shift + V** (tecla maestra) para activar la capa (escucharás un pitido).
2. Suelta las teclas, luego presiona una de las siguientes teclas individuales:

| Tecla           | Función                      | Descripción                                                                 |
|-----------------|------------------------------|-----------------------------------------------------------------------------|
| **Shift + A**   | **Operador de IA**           | **Operación autónoma:** Indica a la IA que realice una tarea en tu pantalla. Presionarlo de nuevo cancela las operaciones activas. |
| **E**           | **Explorador de interfaz**   | **Clic interactivo:** Identifica y hace clic en elementos de la interfaz en cualquier aplicación. |
| **T**           | Traductor inteligente        | Traduce el texto bajo el cursor del navegador o la selección.               |
| **Shift + T**   | Traductor del portapapeles   | Traduce el contenido que hay actualmente en el portapapeles.                |
| **R**           | Refinador de texto           | Resume, corrige gramática, explica o ejecuta **Indicaciones personalizadas**. |
| **V**           | Visión de objeto             | Describe el objeto del navegador actual.                                    |
| **O**           | Visión de pantalla completa  | Analiza el diseño y contenido completo de la pantalla.                      |
| **Shift + V**   | Análisis de vídeo en línea   | Analiza vídeos de **YouTube**, **Instagram**, **TikTok** o **Twitter (X)**. |
| **D**           | Lector de documentos         | Lector avanzado de PDF e imágenes con selección de rango de páginas.        |
| **F**           | **Acción inteligente de archivo** | Reconocimiento contextual desde imagen, PDF o archivos TIFF seleccionados. |
| **A**           | Transcripción de audio       | Transcribe archivos MP3, WAV u OGG a texto.                                 |
| **C**           | Solucionador de CAPTCHA      | Captura y resuelve CAPTCHAs (compatible con portales gubernamentales).      |
| **S**           | Dictado inteligente          | Convierte voz a texto. Presiona para iniciar la grabación, vuelve a presionar para detener/escribir. |
| **Control+L**   | **Asistente en vivo**        | **Copiloto en tiempo real (solo Gemini):** Inicia o finaliza una conversación de voz y pantalla en vivo con el asistente de IA. |
| **I**           | Informe de estado            | Anuncia el progreso actual (por ejemplo, "Escaneando...", "Inactivo").      |
| **L**           | **Etiquetar objeto**         | **Etiquetado semántico con IA:** Etiqueta permanentemente el elemento/icono enfocado actualmente. |
| **Shift + L**   | **Administrar/Escanear etiquetas** | Abre el administrador de etiquetas (si existen etiquetas) o escanea la aplicación en busca de elementos sin nombre. |
| **U**           | Buscar actualizaciones       | Busca manualmente en GitHub la última versión del complemento.              |
| **Espacio**     | Recuperar último resultado   | Muestra la última respuesta de IA en un diálogo de chat para revisión o seguimiento. |
| **H**           | Ayuda de comandos            | Muestra una lista de todos los atajos disponibles.                          |

### 2.1 Atajos del Lector de documentos (dentro del visor)
- **Ctrl + AvPág:** Ir a la siguiente página.
- **Ctrl + RePág:** Ir a la página anterior.
- **Alt + A:** Abrir un diálogo de chat para hacer preguntas sobre el documento.
- **Alt + R:** Forzar un **Nuevo escaneo con IA** usando tu proveedor activo.
- **Alt + G:** Generar y guardar un archivo de audio de alta calidad (WAV/MP3). *Oculto si el proveedor no admite TTS.*
- **Alt + S / Ctrl + S:** Guardar el texto extraído como archivo TXT o HTML.

## 3. Indicaciones personalizadas y variables

Puedes administrar las indicaciones en **Configuración > Indicaciones > Administrar indicaciones...**.

### Variables compatibles
- `[selection]`: Texto seleccionado actualmente.
- `[clipboard]`: Contenido del portapapeles.
- `[screen_obj]`: Captura de pantalla del objeto del navegador.
- `[screen_full]`: Captura de pantalla completa.
- `[file_ocr]`: Seleccionar archivo de imagen/PDF para extracción de texto.
- `[file_read]`: Seleccionar documento para leer (TXT, código, PDF).
- `[file_audio]`: Seleccionar archivo de audio para análisis (MP3, WAV, OGG).

***
**Nota:** Se requiere una conexión a Internet activa para todas las funciones de IA. Los documentos de varias páginas se procesan automáticamente.

## 4. Soporte y comunidad

Mantente actualizado con las últimas noticias, funciones y lanzamientos:
- **Canal de Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** Para informes de errores y solicitudes de funciones.

## 5. Colaboradores del proyecto

Un agradecimiento de corazón a los miembros de nuestra comunidad que apoyan el desarrollo continuo y el mantenimiento de este proyecto con sus generosas contribuciones económicas:

*   **@Alyabani94**
*   **Ali Alamri**
*   **Ilya**
*   **Colaborador anónimo** (`UQDd...CnMY`)
*   **leonardo0216**

*Si deseas apoyar el proyecto económicamente y ver tu nombre aquí, puedes encontrar la opción **Donar** en el menú Herramientas de NVDA (submenú Vision Assistant) o durante el proceso de configuración después de la instalación.*


---
## Cambios para 6.5.0

*   **Asistente en vivo**: Se añadió una función de asistente de voz y pantalla en tiempo real, disponible exclusivamente para el proveedor Google Gemini (o proveedores personalizados compatibles con Gemini). Incluye personalización interactiva de voz y profundidad de razonamiento directamente dentro del diálogo, con reconexión automática al cambiar la configuración.
*   **Proveedor de IA MiniMax**: Se integró MiniMax como proveedor par con soporte multimodal completo (chat, visión, OCR), TTS personalizado con más de 300 voces dinámicas y eliminación automática de bloques de razonamiento (por ejemplo, `<think>...</think>`) de las salidas.
*   **Traducción del visor de documentos**: Se corrigió un error de traducción silencioso para usuarios de NVDA que no usan inglés, asegurando que se envíe el código de idioma estándar de 2 letras a Google Translate en lugar del nombre del idioma localizado.
*   **Reintento de escaneo en lotes de PDF**: Se implementó una lógica de reintento altamente optimizada, separada y silenciosa para el escaneo en lotes de documentos PDF, para evitar cargas redundantes y evitar ventanas emergentes de error perturbadoras durante los reintentos.
*   **Estado del visor de documentos**: Se corrigió un error donde el estado general del complemento (verificado mediante `I`) permanecía bloqueado en "Procesamiento por lotes iniciado" durante escaneos de documentos largos.
*   **Fallo de hilo resuelto**: Se corrigió un fallo grave de aserción de hilo `IsMain() failed in wxTimerImpl` al abrir documentos desde un hilo de fondo, transfiriendo la cola de devolución de llamadas de la GUI a `wx.CallAfter`.

## Cambios para 6.1.2

*   **Verificación previa de etiquetas duplicadas**: Se corrigió un problema en el etiquetado individual donde la verificación de duplicados usaba claves de coordenadas antiguas, lo que hacía que NVDA realizara solicitudes de IA duplicadas para objetos ya etiquetados en lugar de anunciar la etiqueta existente.
*   **Chat de documentos para proveedores que no son Gemini**: Se corrigió una verificación estricta de clave API en el chat de documentos (`on_ask`) para garantizar que los usuarios de OpenAI, Groq o proveedores personalizados locales (como Ollama) puedan chatear con documentos sin ser bloqueados.
*   **Traducción rápida de OCR de Chrome**: Se restauró la API de traducción gratuita y sin clave para el OCR de Chrome. La traducción del texto extraído ahora omite Gemini AI, ahorrando cuotas de API y acelerando el proceso de traducción.
*   **Filtro alfanumérico de CAPTCHA**: Se corrigió la lógica de filtrado en el solucionador de CAPTCHA para garantizar que los caracteres no alfanuméricos se eliminen correctamente en todas las situaciones.
*   **Actualización de ayuda de la capa de comandos**: Se corrigió el atajo de anuncio de estado en el menú de ayuda de `L` a `I`, y se añadieron ambos comandos de etiquetado (`L` y `Shift+L`) a la lista.

## Cambios para 6.1.1

*   **Corrección de salida de Gemma 4 Thinking**: Se corrigió un problema con los modelos Gemma 4 donde todo el proceso de pensamiento interno se mostraba como respuesta final, o donde deshabilitar el pensamiento daba como resultado respuestas vacías. El complemento ahora aísla y extrae correctamente solo el texto de respuesta final limpio.
*   **OCR en lotes desde el Explorador de archivos**: Ahora puedes seleccionar múltiples fotos o PDFs directamente en el Explorador de archivos de Windows y extraer texto o analizarlos en lotes. El complemento filtrará y procesará automáticamente solo los formatos de archivo compatibles.

## Cambios para 6.1.0

*   **Integración universal de IA local (Configurar IA local)**: Se añadió un nuevo botón **"Configurar IA local"** en la configuración del proveedor personalizado. Los usuarios ahora pueden configurar automáticamente motores de IA locales, incluidos **Ollama**, **LM Studio**, **Jan.ai** y **KoboldCPP** al instante.
*   **Omisión inteligente de proxy local**: Se reconstruyó la lógica de conexión con un mecanismo avanzado de omisión de proxy. El complemento ahora es lo suficientemente inteligente como para omitir completamente los proxies del sistema Windows para conexiones de loopback local, garantizando conexiones de IA local estables incluso cuando tu VPN/modo TUN está activo.
*   **Etiquetado de IA ultraestable (v2)**: Se reemplazaron las claves de coordenadas absolutas de pantalla con un sistema avanzado e híbrido de **firma de objeto**. Las etiquetas ahora dependen de identificadores programáticos (UIA **AutomationId** o Win32 **ControlID**) y coordenadas relativas a la ventana, lo que hace que tus etiquetas personalizadas sean completamente resistentes al redimensionamiento, movimiento, cambio de monitor o escalado de ventanas.
*   **Migración automática perfecta de etiquetas**: La actualización es completamente transparente. El complemento migrará automáticamente tus etiquetas antiguas basadas en coordenadas al nuevo formato de huella digital estable en segundo plano al primer enfoque, sin pérdida de datos.

## Cambios para 6.0

*   **Introducción al etiquetado semántico con IA**: Los usuarios ahora pueden etiquetar permanentemente botones e iconos sin nombre usando IA. Presiona **L** para etiquetar el objeto del navegador actual (compatible con el enfoque de tabulación y la navegación de objetos) o **Shift+L** para escanear y etiquetar toda la aplicación de una vez.
*   **Gestión inteligente de etiquetas**: Se añadió un nuevo diálogo de administrador de etiquetas completamente accesible (a través de **Shift+L** si existen etiquetas) para ver, renombrar o eliminar etiquetas personalizadas en lote.
*   **Análisis directo de archivos (omitir diálogo de archivo)**: El complemento ahora es lo suficientemente inteligente como para detectar si estás enfocado en un PDF o archivo de imagen en el Explorador de archivos de Windows. Presionar **F (Acción inteligente de archivo)** o **D (Lector de documentos)** en un archivo resaltado lo procesará inmediatamente, omitiendo por completo el diálogo estándar de "Abrir".

## Cambios para 5.6

*   **Motor OCR "Ninguno (Extraer capa de texto)" añadido**: Los usuarios ahora pueden extraer texto directamente de PDFs con capacidad de búsqueda sin usar créditos de IA, mejorando significativamente la velocidad y privacidad para documentos basados en texto.
*   **Precisión mejorada del Explorador de interfaz**: Se mejoró la indicación del Explorador de interfaz para identificar mejor los tipos de elementos (como elementos de lista) e informar con precisión estados como "(Marcado)", "(Seleccionado)" o "(Expandido)" ignorando componentes del sistema de Windows como la barra de tareas y el reloj.
*   **Recordatorio de configuración de instalación**: Se añadió una notificación después de la instalación para guiar a los usuarios al menú de configuración para configurar sus claves API y preferencias.

## Cambios para 5.5.2

*   **Error de escritura del Operador de IA corregido:** Se resolvió un error donde se escribía la letra 'v' en lugar de pegar texto en ciertos sistemas. Esta corrección aborda conflictos de temporización que ocurrían durante alta carga del sistema.
*   **Estabilidad mejorada:** Se añadió un manejo robusto de errores para las operaciones del portapapeles para evitar fallos del complemento cuando el portapapeles del sistema está temporalmente bloqueado por otras aplicaciones.
*   **Optimización de temporización:** Se ajustaron los retrasos internos para eventos de teclado para garantizar mayor fiabilidad en diferentes velocidades de sistema y mejor compatibilidad con gestores de portapapeles de terceros.

## Cambios para 5.5 (La actualización de automatización)

*   **Operador de IA (Control autónomo - Shift+A):** Esta es la joya de la corona de la v5.5. Vision Assistant Pro ha pasado de ser un asistente pasivo a convertirse en tu **Operador de IA** personal. Ya no solo describe la pantalla, sino que toma el control.
    *   *Cómo funciona:* Ahora puedes dar instrucciones verbales para operar tu PC. Por ejemplo, en una aplicación completamente inaccesible donde tu lector de pantalla permanece en silencio, puedes presionar **Shift+A** y escribir: *"Haz clic en el botón de Configuración"* o *"Encuentra el campo de búsqueda, escribe 'Últimas noticias' y pulsa enter."* La IA identifica visualmente los elementos, mueve el ratón y ejecuta la tarea por ti.
    *   *Nota de rendimiento:* Esta función está optimizada para **Gemini 3.0 Flash (Vista previa)**, ofreciendo respuestas increíblemente rápidas e inteligentes que pueden manejar incluso los diseños de interfaz más complejos.
    *   **⚠️ Advertencia de uso de API:** Dado que el Operador de IA necesita "ver" exactamente lo que está pasando para ser preciso, envía una captura de pantalla de alta resolución con cada paso. Ten en cuenta que el uso frecuente consumirá tu cuota de API mucho más rápido que las tareas estándar basadas en texto.
*   **Explorador visual de interfaz (E):** ¿Cansado de navegar por "botones sin etiqueta"? Presiona **E** para activar el Explorador de interfaz. La IA escaneará toda la ventana y generará una lista de cada elemento en el que se puede hacer clic que ve, incluidos iconos, gráficos y menús. Simplemente elige un elemento de la lista y el Operador de IA hará clic en él por ti. Es como tener una "capa accesible" sobre cualquier aplicación.
*   **Acción inteligente de archivo contextual (F):** La tecla "F" ha sido completamente renovada. Ya no asume que solo quieres OCR. Cuando seleccionas una sola imagen, ahora pregunta de forma inteligente por tu intención: puedes elegir una **Descripción visual detallada** para entender la escena o una **Extracción de texto estructurado (OCR)** para la lectura. El menú se adapta dinámicamente según el tipo de archivo y tu motor de IA activo.
*   **Optimización del núcleo:** Hemos realizado una limpieza profunda de la lógica interna del complemento, eliminando funciones heredadas no utilizadas y código redundante. Esto resulta en una experiencia más ágil, rápida y fiable para todos los usuarios.

## Cambios para 5.0

* **Arquitectura multiproveedor**: Se añadió soporte completo para **OpenAI**, **Groq** y **Mistral** junto a Google Gemini. Los usuarios ahora pueden elegir su backend de IA preferido.
* **Enrutamiento avanzado de modelos**: Los usuarios de proveedores nativos (Gemini, OpenAI, etc.) ahora pueden seleccionar modelos específicos de una lista desplegable para diferentes tareas (OCR, STT, TTS).
* **Configuración avanzada de punto de acceso**: Los usuarios de proveedores personalizados pueden ingresar manualmente URLs específicas y nombres de modelos para un control granular sobre servidores locales o de terceros.
* **Visibilidad inteligente de funciones**: El menú de configuración y la interfaz del Lector de documentos ahora ocultan automáticamente las funciones no compatibles (como TTS) según el proveedor seleccionado.
* **Obtención dinámica de modelos**: El complemento ahora obtiene la lista de modelos disponibles directamente desde la API del proveedor, garantizando compatibilidad con nuevos modelos en cuanto se publiquen.
* **OCR y traducción híbridos**: Se optimizó la lógica para usar Google Translate para mayor velocidad al usar el OCR de Chrome, y traducción con IA al usar los motores Gemini/Groq/OpenAI.
* **"Nuevo escaneo con IA" universal**: La función de reescaneo del Lector de documentos ya no se limita a Gemini. Ahora utiliza cualquier proveedor de IA activo para reprocesar páginas.

## Cambios para 4.6
* **Recuperación interactiva de resultados:** Se añadió la tecla **Espacio** a la capa de comandos, lo que permite a los usuarios reabrir instantáneamente la última respuesta de IA en una ventana de chat para preguntas de seguimiento, incluso cuando el modo de "Salida directa" está activo.
* **Centro de comunidad en Telegram:** Se añadió un enlace al "Canal oficial de Telegram" en el menú Herramientas de NVDA, proporcionando una forma rápida de mantenerse actualizado con las últimas noticias, funciones y lanzamientos.
* **Estabilidad de respuesta mejorada:** Se optimizó la lógica central para las funciones de Traducción, OCR y Visión para garantizar un rendimiento más fiable y una experiencia más fluida al usar la salida de voz directa.
* **Guía de interfaz mejorada:** Se actualizaron las descripciones de configuración y la documentación para explicar mejor el nuevo sistema de recuperación y cómo funciona junto con la configuración de salida directa.

## Cambios para 4.5
* **Administrador avanzado de indicaciones:** Se introdujo un diálogo de gestión dedicado en configuración para personalizar las indicaciones predeterminadas del sistema y administrar las indicaciones definidas por el usuario con soporte completo para agregar, editar, reordenar y previsualizar.
* **Soporte de proxy completo:** Se resolvieron problemas de conectividad de red asegurando que la configuración de proxy del usuario se aplique estrictamente a todas las solicitudes de API, incluidas traducción, OCR y generación de voz.
* **Migración automática de datos:** Se integró un sistema de migración inteligente para actualizar automáticamente las configuraciones de indicaciones heredadas a un formato JSON v2 robusto en el primer inicio sin pérdida de datos.
* **Compatibilidad actualizada (2025.1):** Se estableció la versión mínima requerida de NVDA en 2025.1 debido a las dependencias de biblioteca en funciones avanzadas como el Lector de documentos para garantizar un rendimiento estable.
* **Interfaz de configuración optimizada:** Se simplificó la interfaz de configuración reorganizando la gestión de indicaciones en un diálogo separado, proporcionando una experiencia de usuario más limpia y accesible.
* **Guía de variables de indicaciones:** Se añadió una guía integrada dentro de los diálogos de indicaciones para ayudar a los usuarios a identificar y usar fácilmente variables dinámicas como [selection], [clipboard] y [screen_obj].

## Cambios para 4.0.3
*   **Mayor resiliencia de red:** Se añadió un mecanismo de reintento automático para manejar mejor las conexiones a Internet inestables y los errores temporales del servidor, asegurando respuestas de IA más fiables.
*   **Diálogo visual de traducción:** Se introdujo una ventana dedicada para los resultados de traducción. Los usuarios ahora pueden navegar y leer traducciones largas línea por línea, similar a los resultados de OCR.
*   **Vista formateada agregada:** La función "Ver formateado" en el Lector de documentos ahora muestra todas las páginas procesadas en una sola ventana organizada con encabezados de página claros.
*   **Flujo de trabajo OCR optimizado:** Se omite automáticamente la selección de rango de páginas para documentos de una sola página, haciendo el proceso de reconocimiento más rápido y fluido.
*   **Estabilidad de API mejorada:** Se cambió a un método de autenticación basado en encabezados más robusto, resolviendo posibles errores de "Todas las claves API fallaron" causados por conflictos de rotación de claves.
*   **Correcciones de errores:** Se resolvieron varios fallos potenciales, incluido un problema durante la finalización del complemento y un error de enfoque en el diálogo de chat.

## Cambios para 4.0.1
*   **Lector de documentos avanzado:** Un potente visor nuevo para PDF e imágenes con selección de rango de páginas, procesamiento en segundo plano y navegación fluida con `Ctrl+AvPág/RePág`.
*   **Nuevo submenú de herramientas:** Se añadió un submenú dedicado "Vision Assistant" en el menú Herramientas de NVDA para un acceso más rápido a las funciones principales, configuración y documentación.
*   **Personalización flexible:** Ahora puedes elegir tu motor OCR y voz TTS preferidos directamente desde el panel de configuración.
*   **Soporte de múltiples claves API:** Se añadió soporte para múltiples claves API de Gemini. Puedes ingresar una clave por línea o separarlas con comas en la configuración.
*   **Motor OCR alternativo:** Se introdujo un nuevo motor OCR para garantizar un reconocimiento de texto fiable incluso al alcanzar los límites de cuota de la API de Gemini.
*   **Rotación inteligente de claves API:** Cambia automáticamente y recuerda la clave API que funciona más rápido para evitar límites de cuota.
*   **Documento a MP3/WAV:** Capacidad integrada para generar y guardar archivos de audio de alta calidad en formatos MP3 (128kbps) y WAV directamente dentro del lector.
*   **Soporte de historias de Instagram:** Se añadió la capacidad de describir y analizar Historias de Instagram usando sus URLs.
*   **Soporte de TikTok:** Se introdujo soporte para vídeos de TikTok, permitiendo descripción visual completa y transcripción de audio de clips.
*   **Diálogo de actualización rediseñado:** Cuenta con una nueva interfaz accesible con un cuadro de texto desplazable para leer claramente los cambios de versión antes de instalar.
*   **Estado y experiencia de usuario unificados:** Se estandarizaron los diálogos de archivos en todo el complemento y se mejoró el comando 'L' para informar el progreso en tiempo real.

## Cambios para 3.6.0
*   **Sistema de ayuda:** Se añadió un comando de ayuda (`H`) dentro de la capa de comandos para proporcionar una lista fácilmente accesible de todos los atajos y sus funciones.
*   **Análisis de vídeos en línea:** Se amplió el soporte para incluir vídeos de **Twitter (X)**. También se mejoró la detección de URL y la estabilidad para una experiencia más fiable.
*   **Contribución al proyecto:** Se añadió un diálogo de donación opcional para los usuarios que deseen apoyar las futuras actualizaciones y el crecimiento continuo del proyecto.

## Cambios para 3.5.0
\*   \*\*Capa de comandos:\*\* Se introdujo un sistema de capa de comandos (predeterminado: `NVDA+Shift+V`) para agrupar los atajos bajo una sola tecla maestra. Por ejemplo, en lugar de presionar `NVDA+Control+Shift+T` para traducción, ahora presionas `NVDA+Shift+V` seguido de `T`.
\*   \*\*Análisis de vídeos en línea:\*\* Se añadió una nueva función para analizar vídeos de YouTube e Instagram directamente proporcionando una URL.

## Cambios para 3.1.0
*   **Modo de salida directa:** Se añadió una opción para omitir el diálogo de chat y escuchar las respuestas de IA directamente a través de voz para una experiencia más rápida y fluida.
*   **Integración con portapapeles:** Se añadió una nueva configuración para copiar automáticamente las respuestas de IA al portapapeles.

## Cambios para 3.0

*   **Nuevos idiomas:** Se añadieron traducciones al **persa** y **vietnamita**.
*   **Modelos de IA ampliados:** Se reorganizó la lista de selección de modelos con prefijos claros (`[Gratis]`, `[Pro]`, `[Auto]`) para ayudar a los usuarios a distinguir entre modelos gratuitos y con límite de uso (de pago). Se añadió soporte para **Gemini 3.0 Pro** y **Gemini 2.0 Flash Lite**.
*   **Estabilidad del dictado:** Se mejoró significativamente la estabilidad del Dictado inteligente. Se añadió una verificación de seguridad para ignorar los clips de audio de menos de 1 segundo, evitando alucinaciones de IA y errores vacíos.
*   **Gestión de archivos:** Se corrigió un problema donde la carga de archivos con nombres no ingleses fallaba.
*   **Optimización de indicaciones:** Se mejoró la lógica de traducción y los resultados de Visión estructurados.
## Cambios para 2.9

*   **Se añadieron traducciones al francés y turco.**
*   **Vista formateada:** Se añadió un botón "Ver formateado" en los diálogos de chat para ver la conversación con el estilo adecuado (encabezados, negrita, código) en una ventana de navegación estándar.
*   **Configuración de Markdown:** Se añadió una nueva opción "Limpiar Markdown en el chat" en la Configuración. Desmarcarla permite a los usuarios ver la sintaxis de Markdown sin procesar (por ejemplo, `**`, `#`) en la ventana de chat.
*   **Gestión de diálogos:** Se corrigió un problema donde las ventanas de "Refinar texto" o chat se abrían varias veces o no se enfocaban correctamente.
*   **Mejoras de experiencia de usuario:** Se estandarizaron los títulos de los diálogos de archivos a "Abrir" y se eliminaron los anuncios de voz redundantes (por ejemplo, "Abriendo menú...") para una experiencia más fluida.

## Cambios para 2.8
* Se añadió traducción al italiano.
* **Informe de estado:** Se añadió un nuevo comando (NVDA+Control+Shift+I) para anunciar el estado actual del complemento (por ejemplo, "Cargando...", "Analizando...").
* **Exportación HTML:** El botón "Guardar contenido" en los diálogos de resultados ahora guarda la salida como un archivo HTML formateado, preservando estilos como encabezados y texto en negrita.
* **Interfaz de configuración:** Se mejoró el diseño del panel de configuración con agrupación accesible.
* **Nuevos modelos:** Se añadió soporte para gemini-flash-latest y gemini-flash-lite-latest.
* **Idiomas:** Se añadió el nepalí a los idiomas compatibles.
* **Lógica del menú Refinar:** Se corrigió un error crítico donde los comandos de "Refinar texto" fallaban si el idioma de la interfaz de NVDA no era inglés.
* **Dictado:** Se mejoró la detección de silencio para evitar la salida de texto incorrecta cuando no se ingresa voz.
* **Configuración de actualizaciones:** "Buscar actualizaciones al iniciar" está ahora deshabilitado de forma predeterminada para cumplir con las políticas de la tienda de complementos.
* Limpieza de código.

## Cambios para 2.7
* Se migró la estructura del proyecto a la plantilla oficial de complementos de NV Access para un mejor cumplimiento de estándares.
* Se implementó lógica de reintento automático para errores HTTP 429 (Límite de velocidad) para garantizar fiabilidad durante el tráfico alto.
* Se optimizaron las indicaciones de traducción para mayor precisión y mejor manejo de la lógica de "intercambio inteligente".
* Se actualizó la traducción al ruso.

## Cambios para 2.6
* Se añadió soporte de traducción al ruso (Gracias a nvda-ru).
* Se actualizaron los mensajes de error para proporcionar comentarios más descriptivos sobre la conectividad.
* Se cambió el idioma de destino predeterminado al inglés.

## Cambios para 2.5
* Se añadió el comando de OCR de archivos nativo (NVDA+Control+Shift+F).
* Se añadió el botón "Guardar chat" a los diálogos de resultados.
* Se implementó soporte completo de localización (i18n).
* Se migró la retroalimentación de audio al módulo de tonos nativo de NVDA.
* Se cambió a la API de archivos de Gemini para un mejor manejo de archivos PDF y de audio.
* Se corrigió el fallo al traducir texto que contiene llaves.

## Cambios para 2.1.1
* Se corrigió un problema donde la variable [file_ocr] no funcionaba correctamente dentro de las Indicaciones personalizadas.

## Cambios para 2.1
* Se estandarizaron todos los atajos para usar NVDA+Control+Shift y eliminar conflictos con el diseño de portátil de NVDA y los métodos abreviados del sistema.

## Cambios para 2.0
* Se implementó el sistema de actualización automática incorporado.
* Se añadió la caché de traducción inteligente para la recuperación instantánea de textos traducidos previamente.
* Se añadió la memoria de conversación para refinar contextualmente los resultados en los diálogos de chat.
* Se añadió el comando dedicado de traducción del portapapeles (NVDA+Control+Shift+Y).
* Se optimizaron las indicaciones de IA para aplicar estrictamente la salida en el idioma de destino.
* Se corrigió el fallo causado por caracteres especiales en el texto de entrada.

## Cambios para 1.5
* Se añadió soporte para más de 20 nuevos idiomas.
* Se implementó el diálogo interactivo de refinado para preguntas de seguimiento.
* Se añadió la función de Dictado inteligente nativo.
* Se añadió la categoría "Vision Assistant" al diálogo de Gestos de entrada de NVDA.
* Se corrigieron los fallos de COMError en aplicaciones específicas como Firefox y Word.
* Se añadió el mecanismo de reintento automático para errores del servidor.

## Cambios para 1.0
* Lanzamiento inicial.

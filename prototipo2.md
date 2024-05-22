Enlace del proyecto en Github por si no se puede ver desde el Gitlab: https://github.com/A22JulioAA/legal_code

# Prototipo 2 - Proyecto Final
Julio Aller Acuña - 2º DAW Ordinario

---

#### Objetivos propuestos:
Los objetivos marcados para este prototipo en el prototipo anterior, en su mayoría, no han sido completados. El motivo es que en un principio la idea era separar los distintos tipos de usuarios, clientes y profesionales. En el transcurso del desarrollo se ha decidido permitir solamente el registro como cliente y establecer unos profesionales de base.
Los objetivos y avances sí cumplidos son los siguientes:
- **Implementación completa del registro/inicio de sesión:** Se ha conseguido implementar completamente la función de registro del usuario(cliente) y la de inicio de sesión. Ambas con estrictas medidas de seguridad como encriptado de contraseñas, protección contra ataques CSRF y validación de datos. Con esto conseguimos que cada usuario tenga una experiencia personalizada, con su propia página de perfil, citas, calendario etc.
- **Implementación de páginas de citas:** Se han implementado dos páginas en referencia con la solicitud de citas con profesionales. Por un lado la que permite a los usuarios concertar la cita, con posibilidad de escoger la fecha y hora y establecer un motivo de la visita. Por defecto todas las citas están PENDIENTES, lo que significa que se llevarán a cabo, pero en próximas versiones, cuando la parte de profesionales esté implementada estos podrán valorar el motivo y aceptarlas o rechazarlas. Por otro lado tendríamos la página que permite a los usuarios visualizar, anular o modificar sus citas, exclusivas del usuario que tenga la sesión iniciada. 
- **Implementación gráfica del calendario:** Está implementada la parte gráfica del calendario, el cual muestra por defecto la fecha actual. Para este prototipo no se ha añadido funcionalidad más que la de visualizar un simple calendario.
- **Implementación de páginas extra:** Están implementadas páginas a modo de información como pueden ser la de 'Sobre Nosotros' o la de 'Términos y Condiciones de cancelaciones'. Son páginas puramente estéticas e informativas y no realizan función alguna más que la de ayudar al usuario a tener claros posibles problemas.
- **Implementación de página de perfil:** Se ha implementado la parte gráfica del perfil del usuario autenticado en ese momento. Actualmente no pueden hacerse modificaciones de datos del usuario, solamente salir de la sesión y eliminar el perfil, con la consecuente eliminación de datos asociados, como citas.
- **Anuncios y filtros:** Se ha mejorado mucho la presentación de los anuncios de profesionales en la página principal, haciendolo más armónico y agradable visualmente. Se ha añadido un filtro de especialidades para los profesionales y, a partir de la especialidad seleccionada, otro filtro más para el area. Esto hace que se pueda llegar a filtrar de forma bastante precisa. La parte de la especialidad funciona perfectamente, la del campo todavía no.
- **Sección de comentarios:** Se ha implementado la parte visual de los comentarios en cada anuncio, pero no está implementada la funcionalidad. Actualmente es inexistente la posibilidad de comentar acerca de los profesionales.
- **Estética general de la web:** Se ha mejorado de manera considerable la estética de la página, haciendola mucho más agradable. Como apunte especial se han utilizado ilustraciones para complementar muchas de las secciones como 'Sobre Nosotros' o 'Mis Citas'. Estas hacen de la experiencia de usuario mucho más amena y estética.

#### Retos e innovación: 
En este prototipo se han propuesto varios retos como los que se van a comentar a continuación.
- **FullcalendarJS** Esta biblioteca de JavaScript ha sido todo un reto para este proyecto, pues han surgido varios problemas con su uso, pero se intentará seguir implementándolo para el prototipo final, pues es muy versátil y útil de cara a mejorar la experiencia del usuario.
- **Herramientas de Python** Se ha propuesto mejorar el desarrollo pero desde un punto de vista más analítico, aprendiendo a usar diferentes herramientas de Python para debuguear la aplicación, ver tiempos de respuesta de las diferentes secciones, cargas de trabajo para la base de datos etc.
- **Creación de modelos propios** Aunque se haya hecho ya con otros objetos como las Citas, los Profesionales y demás, la creación de una gestión de usuarios propia en Django ha sido un reto. Esto debido a que Django por defecto usa sus propios modelos de perfiles, y al querer usar un modelo propio ha habido que tocar muchas configuraciones y sobreescribir muchas clases. Finalmente se ha conseguido implementar todo de manera consistente y segura.

#### Previsión Prototipo 2:
En el prototipo final está claro el objetivo: finalizar todos los frentes abiertos atualmente. Implementar completamente el calendario, hacer los filtros completamente funcionales e implementar los comentarios, así como permitir al usuario modificar los datos de su perfil. A mayores, como es obvio, siempre se buscará el mejorar la calidad de la web, tanto estéticamente como en materia de rendimiento. Pequeños objetivos serían mejorar el aspecto de algunos títulos, mejorar la disposición de elementos en los anuncios y más ajustes estéticos. Todo esto sin olvidar el asegurarse de que la página sea totalmente accesible y responsiva.


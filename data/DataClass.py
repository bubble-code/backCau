class DataClass:
    def __init__(self):
        self.text = """
Gestión de Artículos
Los artículos son una de las bases principales para el uso de la aplicación, por ello se denominan “Maestro de Información”. Tendremos especial cuidado al realizar los registros de los artículos ya que de ello depende el correcto funcionamiento del sistema.
En este manual veremos cómo realizar la Clasificación de los Artículos, la Información de la Ficha del Artículo, el proceso de Registro y los procesos asociados al Alcance funcional que requiramos.
Además, junto a la información anterior incluimos y detallamos la operativa de la Gestión de Stocks, esto es, la configuración y gestión de las existencias para una correcta planificación y control del almacén o almacenes de la empresa.

Clasificación
Debemos entender un artículo no sólo como el producto que se comercializa o fabrica. Un artículo puede ser una Mercadería o los Servicios que ofrecemos, también la Materia Prima o los Semielaborados (producto que aunque no sea el producto final de su proceso de producción, desea llevar un control de stock y de costes, por ejemplo), un nivel de agrupación para varios artículos, etc. Esto hace que un artículo pueda tener una estructura que deberá definir, así como un alcance que deberá indicar: ¿controlo o no su stock?, ¿es un artículo comercializable?, ¿es un kit?, etc…
Antes de iniciar el registro de cualquier artículo debemos analizar cuáles son los grupos o Tipos de Artículos en los que vamos a clasificar nuestras referencias. Debemos tener en cuenta que, de cara a poder ofrecer un Catálogo de productos debemos realizar una clasificación, es decir, saber las categorías o familias de artículos con los que vamos a operar (Tipos, Familias y Subfamilias).
Por ejemplo, una clasificación inicial estándar podría ser: Existencias Comerciales, Materias Primas y Otros Aprovisionamientos. Donde cada uno de estos grupos puede estar organizado por Familias y Subfamilias.
Esta clasificación nos permitirá tener agrupaciones que posteriormente podremos utilizar para mejorar nuestros procesos. Por ejemplo, en procesos comerciales podremos generar descuentos para un grupo (Tipo/Familia) de artículos específico.

Información y Registro
El Maestro de Artículos es una pieza fundamental para la gestión de nuestra gestión global y es por este motivo que debemos entender correctamente la operativa de clasificación, registro y gestión. Veamos a continuación de forma breve, cómo el estado o el bloqueo de artículos ponen de manifiesto la necesidad de realizar un correcto análisis de la información requerida durante el proceso de registro del maestro de artículos.

Estados/Bloqueos
El control de Estados del artículo permite realizar una gestión de la evolución y operativa de los mismos. Si un artículo se encuentra en estado de homologación, por ejemplo, el sistema puede ser configurado para impedir su expedición. Por otro lado, podemos "desactivar" artículos obsoletos e incluso Bloquear artículos por cliente para impedir inciar procesos comerciales hasta que se regularice determinada situación.
En definitiva, llevar un control de estados en los artículo será beneficioso en varios aspectos. Por un lado nos permitirá saber qué artículos de mi base de datos se encuentran activos en mis actividades y por otra mantendrá un histórico sobre los artículos obsoletos determinantes para realizar valoraciones en almacenes de material remanente.

Alcance Funcional
El Maestro de Artículos incide en casi todos los procesos de la aplicación por lo que el manual está en su mayoría vinculado con los manuales de dichos procesos.
Es por este motivo que no será necesario ralizar el registro de todos los datos de la ficha del artículo sino que únicamente deberá ceñirse a los que operen en el alcance de su actividad.
En el presente manual identificamos cada apartado de información con la funcionalidad vinculada al mismo a fin de determinar las fases de registro conforme se utilice una referencia en uno u otro módulo de la aplicación (ventas, producción, proyectos, etc).
Es importante realizar un análisis inicial de las referencias a registrar como Artículos a fin de determinar en primer lugar la Clasificación o Tipos de Artículos ya que el alcance funcional se establece a nivel del Tipo de Artículo.

Categorías TPV
Un ejemplo de la particularidad de gestión de los artículos reside en los aspectos que requiere para realizar correctamente las funciones esperadas. En el apartado de Clasificación atendíamos a los Tipos de Artículos que nos permiten confeccionar el catálogo de nuestros productos para asociarle una tarifa de venta, por ejemplo. Sin embargo, en determinadas áreas funcionales del circuito de venta nos encontramos con otras necesidades como puede ser el mostrar en los Terminales de Venta un "árbol de categorías" que nos permita seleccionar de forma directa e intuitiva los artículos que operan en las ventas TPV.
El sistema proporciona una herramienta para "construir" gráficamente este árbol de Categorías TPV en paralelo a la Tipología de Artículos creada para otras operaciones de gestión y control de tipo administrativo financiero.

Gestión de Stocks
Solmicro ERP Stocks nos permite llevar el control de las existencias, para poder saber en cualquier momento: ¿Qué cantidad y qué valor tienen los artículos que tengo en los almacenes?.
En primer lugar debemos tener en cuenta que para gestionar nuestro stock deberemos tener cierta información registrada en el sistema:
Artículos: registrar el producto y configurar el uso de Stocks.
Almacenes: registrar nuestros almacenes con sus correspondientes ubicaciones (si trabajamos con almacenes compartimentalizados).
Tipos de Movimientos: indicamos qué clase de movimiento se realizan en los almacenes, si estamos sacando o metiendo material o bien tratando con un ajuste por Inventario que no necesariamente es entrada ni salida.
Los Criterios de Valoración y las Cuentas contables para la Valoración del almacén, los Inventarios y la Regularización de existencias. Es decir, la gestión de Stocks también nos permite obtener la información contable del cierre de inventario para su posterior envio y gestión en el área de Contabilidad del módulo Financiero.
Una vez registrada esta información podremos empezar a realizar los procesos de la gestión de Stocks.

Realizar los Inventarios.
Controlar nuestros Almacenes.
Por un lado podremos realizar la entrada y salida de material. Este proceso se realiza durante los procesos de recepción en compras y expedición en ventas, o bien desde la fabricación, con el control de consumibles y materia prima, así como los productos terminados.
Generar movimientos que no se encuentren vinculados a ningun proceso gestionable. Realizar ajustes, transferencias, y llevar un histórico de todos los movimientos realizados.
Valorar los almacenes. Proceso con el que podremos saber siempre el valor de nuestros almacenes, tanto el valor actual como el valor de una fecha determinada. Igualmente podremos utilizar cualquiera de los criterios de valoración de almacén: FIFO, LIFO, Última Compra, Precio Estándar y Precio Medio.
Finalmente se realiza el Cierre del Inventario obteniendo la información contable para el posterior paso, la Regularización de Existencias en el módulo de contabilidad.
La Gestión de Stocks incorpora una serie de herramientas que nos permitirán trabajar mas a fondo con nuestro stock, podremos:Planificar nuestros almacenes: podremos establecer cuándo realizar el aprovisionamiento de nuestros almacenes así como mantener el nivel de existencias para evitar o atender roturas de stock.
Utilizaremos para ello la gestión del Punto de Pedido, el Stock de Seguridad y el Lote Mínimo de Fabricación.
Gestión de Stock Negativo: que nos permitirá bien, evitar realizar expediciones cuando no tengamos material en stock, o bien, si llevamos un buen control de aprovisionamiento, podremos configurar nuestro sistema para que podamos realizar expediciones de material que aunque no tengamos existencias, sepamos que contaremos con el en una fecha determinada.
Gestión de nuestros artículos por Lotes.
Gestionar nuestros artículos con Números de Serie.
Gestionar la devolución de envases retornables.
Si trabajamos con más de una unidad de almacenamiento por artículo, podremos llevar una gestión de doble unidad.
Inventarios Permanentes.
Artículos Obsoletos.
Kits de Artículos.
Almacenes de Depósito (almacenes "de cliente").
Además de estos procesos, tendremos a nuestra disposición todas las estadísticas necesarias para poder consultar la disponibilidad y trazabilidad de las referencias durante la gestión del stock.

Clasificación de Artículos
La clasificación de artículos consiste en establecer una tipificación para nuestras referencias o artículos, proceso que se realiza en Tipos de Artículos.
Esta clasificación nos permite:
Definir en qué ámbitos van a participar los artículos, es decir el alcance funcional: artículos que únicamente compra y / o vende, los fabrica, etc. De esta forma contribuye a establecer sistemas de control sobre las acciones de trabajo, por ejemplo, solo accederá a conocer el valor de su almacén de aquellos artículos que tengan gestión de stock, o más sencillo, solo puede vender aquellos artículos que tengan asociado un tipo de artículo de ☑ Venta.
Generar tarifas de venta a partir de la tipificación de las referencias, utilidad importante si trabaja con un catálogo de producto.
Asociar Cuentas contables o Descuentos comerciales comunes a Familias de artículos.
Codificar automáticamente los artículos a partir de los identificadores de Tipo y Familia de artículo.
Establecer los Criterios de valoración de almacenes asociados al tipo de artículo.
Generar Estadísticas agrupando la información por Tipos, Familias y / o subfamilias de artículos.

Tipos de Artículos
El primer paso del registro de las referencias, artículos o productos con los que vamos a operar, consiste en establecer los Tipos de Artículos.
Por ejemplo:
Tipo 1: Mercaderías/Existencias Comerciales.
Familias = Categorías de Producto.
Tipo 2: Servicios.
Tipo 3: Materias Primas.
Tipo 4: Otros Aprovisionamientos.
Tipo 5: Embalajes.
 
Estructura y Niveles de Información
A tener en cuenta cómo es la estructura de datos del Tipo de Artículo y qué operativa tiene asociado cada nivel de la estructura: Tipos, Familias y Subfamilias.

Datos de Familias/Subfamilias de Artículo
Las Familias/Subfamilias representan un segundo nivel de clasificación y son dato obligatorio en el registro de cada una de las referencias de artículos.
Permite asociar a cada Familia las cuentas contables o descuentos comerciales que se necesite trasladar a los artículos. También permiten asociar las Características para configurar la gestión de tallas y colores del TPV o bien la generación automática de artículos que tengan en común una referencia global (tallas y colores).
A su vez, por cada familia se pueden establecer distintas subfamilias que otorgan un nivel adicional de análisis en el ámbito estadístico y también la codificación automática de sus artículos por tipo, familia y subfamilia.

Crear un Tipo de Artículo
Accede a Tipos de Artículos.
Indica los datos obligatorios: Código, Descripción y las opciones del Alcance Funcional.
Otros Datos:
Recalcular valoración en movimientos de salida y Criterio de Valoración: datos relacionados con la gestión del stock. Se establecen a nivel del Tipo de Artículoy pasan al Artículo (apartado Almacenes) de forma predeterminada con el objetivo de facilitar el registro y gestión de referencias pudiéndose modificar en el artículo.
Código, Código Abreviado y Descripción Abreviada: Son datos necesarios para la Codificación Automática Avanzada de Artículos.
Color: dato relacionado con la estructura gráfica de las referencias que participan en la gestión del proceso productivo. En la ficha de los productos que cuentan con una estructura de componentes puede acceder a la representación gráfica donde se muestran cada uno de los componentes representados por el color asociado al tipo de artículo al que pertenecen. Para asociar un color al artículo: pulsa sobre el botón  y selecciona de la paleta de colores, el color que deseas asociar al tipo.
Imagen: dato relacionado con la representación por imágenes de las referencias o catálogo de producto. Se utiliza en Solmicro ERP TPV.
Accede a las líneas y crea, al menos, una Familia por Tipo de Artículo.

Nueva Familia-Subfamilia
Al menos debe existir una Familia por Tipo de Artículo.
Proceso:
Accede a Tipos de Artículos.
En el Tipo de Artículo, acude a las líneas.
Indica los datos obligatorios: Código y Descripción de la Familia.
Correlativo: número correlativo utilizado en la codificación automática simple de artículos.
Característica 1, 2, 3,4 y 5: permite indicar qué características se van a gestionar en la gestión de tallas y colores.
% Recepción Máxima: este es un dato para las recepciones de mercancía (Compras), aquí indicaremos el porcentaje de exceso de material que podremos soportar en cada envío a nivel de familia. Por ejemplo, si establecemos un 20% de recepción máxima, en caso de que tengamos una compra de 100 unidades de un artículo correspondiente a esta familia, únicamente podremos crear el albarán de recepción de hasta 120 unidades, las demás se tendrán que devolver al proveedor.
Código, Código Abreviado y Descripción Abreviada: Son datos necesarios para la codificación automática de artículos avanzada.
 Subfamilias: representan el tercer nivel de clasificación junto al tipo y la familia, principalmente esta información se asocia al artículo y posteriormente se utiliza con fines estadísticos. Además de este alcance, las subfamilias pueden también participar en la codificación automática de artículos. Para crear subfamilias, pulse sobre este botón, e indique los datos:
Código y descripción identificativa de la subfamilia.
Correlativo: número correlativo utilizado en la codificación automática simple de artículos.
% Recepción Máxima: este es un dato para las recepciones de mercancía (Compras), aquí indicaremos el porcentaje de exceso de material que podremos soportar en cada envío a nivel de subfamilia. Por ejemplo, si establecemos un 20% de recepción máxima, en caso de que tengamos una compra de 100 unidades de un artículo correspondiente a esta subfamilia, únicamente podremos crear el albarán de recepción de hasta 120 unidades, las demás se tendrán que devolver al proveedor.
Código, Código Abreviado y Descripción Abreviada: Son datos necesarios para la codificación automática avanzada.
Características: no confundir con las características de la gestión de tallas y colores. Estas características se trasladan a la solapa ‘Características’ de la ficha del artículo a fin de informar de los valores correspondientes. Posteriormente esta información se utiliza por ejemplo, en la gestión de alquileres para facilitar la búsqueda y localización de referencias (ejemplo: remolques cuyo tonelaje es superior a las 2 TN, etc.).
 Descuentos comerciales 123 por familia: aspecto utilizado en la gestión de tarifas de venta.
 Cuentas contables por familia: de forma que le facilite la gestión y registro de nuevas referencias de artículos ya que estos valores pasan de forma predeterminada (solapaGeneral: Cuentas contables por familia) a la ficha del artículo. Para establecer las cuentas contables de una familia pulse sobre este botón e indique los datos de las cuentas contables que ha de establecer por familia de artículos:
Se establecen tanto las cuentas contables individuales como las cuentas contables de grupo. Aspecto relacionado con dos puntos de vista:
En la ficha del artículo no será necesario recoger cuentas contables individuales, si existen cuentas asociadas a la familia del artículo.
Si existe dato para el cliente en el campo ‘Empresa Grupo’ (ficha cliente >> solapa ‘Cuentas Contables’),
El sistema recoge las cuentas contables asociadas al grupo del artículo.
Este listado de cuentas contables se muestra en la ficha del artículo > solapa ‘Cuentas Contables’ > sub-solapa ‘Cuentas Familia’. El sistema utilizará este listado de cuentas siempre y cuando no exista información en la cuenta contable asociada al artículo activo.
 Asociar imágenes por familia: se utilizan para indicar la imagen que representará gráficamente la familia en las pantallas de los terminales TPV. Para asociar una imagen pulse sobre este botón, el sistema la pantalla ‘Ver / Modificar Imagen’, pulsando sobre esta pantalla donde a través del menú contextual podrá realizar estas acciones (mismo que el proceso ‘Asociar imagen a un artículo’).

Información de Artículos
A continuación detallamos los parámetros funcionales y los maestros de información auxiliar necesaria para la correcta gestión de los artículos.
Posteriormente, en el apartado Datos del Artículo ampliaremos la información en función del alcance funcional de cada uno de los apartados.

Mantenimientos Auxiliares
Estados de Artículo
Muestra la información correspondiente a los distintos Estados susceptibles de asociar a cada uno de los artículos, productos o referencias.
Permite crear nuevos Estados que permitan identificar fases de la evolución de los artículos, como por ejemplo, los artículos obsoletos.
Proceso:
Acude a Estados de Artículos.
Datos:
Estado: código identificador del estado de artículo.
Descripción Estado: descripción detallada del Estado.
Activo: implica entradas y salidas de stock.
Visible TPV: se muestra en las de Venta TPV.
Efectos:
En la información del artículo se registra/muestra el Estado y la opción ☑ Disponible, activa o no, en función del valor de la opción ☑ Activo asociado al Estado.
Funcionalidad Asociada
Logística - Compras y Ventas: si el Estado implica que el artículo no está activo, disponible, el sistema no permitirá realizar movimientos de stock (recepciones, expediciones, etc).
TPV: en los terminales punto de venta solo se mostrarán los artículos cuyo Estado implique que está activo/disponible.

Unidades de Medida
Muestra la información correspondiente a las distintas Unidades de Medida susceptibles de asociar a las cantidades de cada uno de los artículos, productos o referencias en las distintas operaciones en las que participan.
Permite crear nuevas Unidades que se ajusten a la operativa de almacenaje, comercial o fabricación de la empresa.
Proceso:
Acude a Unidades de Medida.
Datos:
Unidad: código identificador de la unidad de medida.
Descripción Unidad: descripción detallada de la unidad de medida.
Código Factura-e: códigos utilizados en los ficheros de la factura electrónica.
Tipo Embalaje: XXX.
Efectos:
En la información del artículo (apartado Unidades/Precios) se registran/muestran las Unidades empleadas en los circuitos de Venta, Compra y Almacén del artículo. El sistema asocia por defecto la Unidad de Medida establecida en los parámetros generales.
Funcionalidad Asociada
Logística - Compras y Ventas: si el Estado implica que el artículo no está activo, disponible, el sistema no permitirá realizar movimientos de stock (recepciones, expediciones, etc).
TPV: en los terminales punto de venta solo se mostrarán los artículos cuyo Estado implique que está activo/disponible.

Conversiones Genéricas
Listado de correspondencias entre las distintas unidades de medida identificando los factores de conversión.
Datos:
Unidad A: indicaremos la unidad A. En la operativa posterior, se corresponderá con la Unidad Venta, Unidad Compra o Unidad Fábrica.
Unidad B: indicaremos la unidad B. En la operativa posterior, se corresponderá con la Unidad Interna.
Factor:equivalencia entre ambas unidades. Entendiendo Unidad A = Factor * Unidad B.
Ejemplo:
Somos una empresa productora y distribuidora de vinos. El proceso productivo se inicia en nuestros propios viñedos. El vino llega a nuestras naves y se almacena en Depósitos de diferente capacidad, pero siempre considerando la Unidad de almacenamiento, el litro. La venta al cliente 01 se realiza en la unidad de venta: botella "normal" de 75 cl. y para el cliente 02 en la unidad de venta: botella "magnum" de 1,5 lt. El precio de venta se establece por cada tipo de botella. En ocasiones compramos vinos de otros viñedos. En estos casos compramos depósitos completos, con lo que la unidad de compra será el depósito de X litros.
El sistema mostrará en cada operación (venta, compra o embotellado) las cantidades tanto en la unidad interna de almacenamiento, como en la unidad que corresponda a la operación por lo que obtenemos una gestión de la doble unidad en todos los circuitos de Solmicro ERP.

Datos del Artículo
Debemos registrar una FICHA DE ARTICULO por cada una de las referencias con las que operamos: servicios, material, etc., tanto si tienen gestión comercial como si son de consumo interno. En definitiva, cualquier artículo que nos interese ver reflejado que aunque no conlleve una operativa propia sea susceptible a algún tipo de explotación de información. Asímismo debemos tener en cuenta en todo momento el alcance de la gestión de nuestro artículo, para saber qué información es la fundamental para realizar el registro y qué información no influye en nuestra gestión.

Gestión de Artículos (Procesos)
Registro de Artículos
¿Cómo incorporar los Artículos al sistema?
Existen dos formas de dar de alta los artículos al sistema: con la migración de los datos mediante la importación de ficheros o con el registro manual directamente en el sistema, ingresando los datos de nuestros artículos uno a uno.
Independientemente de la forma en la que realice el registro se recomienda realizar un análisis detallado de la aplicación de cada referencia de artículos en la actividad de la empresa para identificar su alcance funcional y determinar qué información se requiere en cada caso y situación.
1. Registro de la Información Previa
Se trata de información auxiliar necesaria para registrar la información del artículo. Además de la información general del sistema (manual de Configuración Inicial) debemos revisar/registrar los Mantenimientos Auxiliares de los Artículos.
2. Alta de Artículos: Masiva / Manual
Para realizar el registro masivo utilizaremos la herramienta de importación masiva que le proporciona la aplicación. Este proceso se puede consultar en el manual del Manejo de la Aplicación.
Para realizar el registro manual de artículos:
Analiza la Clasificación (Tipos/Familias/Subfamilias) de artículos que van a operar tanto en los procesos de compra como en los procesos de comercialización, producción, etc.
Si procede, analiza cómo se van a Codificar las referencias a registrar para utilizar Contadores o configurar la Codificación Avanzada de artículos.
Registra la clasificación en los Tipos de Artículos.
Importante: ten en cuenta que al registrar una nueva referencia (artículo) y tras asociarle un Tipo y Familia, el sistema muestra las opciones ‘heredadas’ del alcance funcional establecido en el Tipo. No son modificables en la ficha del artículo.
Configura los Contadores o los Criterios para la Codificación Avanzada de artículos.
Inicia el registro de los Artículos. Los Datos obligatorios son: Código, Descripción, Tipo, Familia, Estado y Fecha de Alta.
3. Registro de detalle (alcance funcional)
Tras la realización del registro inicial y conforme vaya creciendo el uso de su aplicación irá incorporando otros aspectos de interés:
Datos financieros: tipo de IVA asociado al artículo, por ejemplo.
Datos logísticos: en qué almacenes hay disponibilidad de existencias, cuál va a ser el criterio de almacén utilizado, qué unidades de almacenamiento o qué embalajes va a utilizar, etc.
Datos de gestión: clientes y/o proveedores habituales.
Datos técnicos: revisiones por artículo o por artículo - cliente y/o artículo - proveedor, documentación exigida por el departamento de Calidad, documentación técnica (herramienta de Gestión Documental).
Toda esta información la encontrará detallada en el apartado de Datos del Artículo de este manual.

Estados del artículo
Artículos Obsoletos
Por defecto, el sistema asocia el Estado de artículo establecido en el parámetro general: ‘Estado predeterminado’.
Si desea indicar que un artículo ha quedado obsoleto simplemente debe cambiar su Estado.
El control del artículo obsoleto se realiza en ventas, compras y producción, en estos se verifica que el artículo:
Ventas: pertenezca a un tipo de artículo con la característica “venta” + que el estado del artículo esté activo.
Compras: pertenezca a un tipo de artículo con la característica “compra” + que el estado del artículo esté activo.
Producción: pertenezca a un tipo de artículo con la característica “fábrica” + que el estado del artículo esté activo.
La gestión del stock no se realiza esta comprobación ya que en este caso impediríamos realizar movimientos de procesos generados anteriormente al cambio de estado del artículo.
Por ejemplo, en un inventario no nos influye el que un artículo esté obsoleto o no ya que el hecho a evaluar es si hay o no existencias en el almacén, lo mismo ocurre con la valoración de almacenes, en este proceso lo que nos interesa es saber el valor de mis existencias independientemente de que estos artículos estén obsoletos o no.
En definitiva el control de activo/no activo de un artículo impedirá realizar procesos del tipo comercial / compras y fabricación, pero no su consideración como inventario ya que no “desaparece” del almacén por este hecho.
Activo: Si esta marca está desactivada no se permiten ni entradas ni salidas de stock. Esta opción se haya vinculada al Estado asociado al artículo, por lo que el que esté activo  o no dependerá del estado asociado, por ejemplo una referencia cuyo estado es ‘obsoleto’ no se encontrará activo por lo que no podrá ser ni recibido, ni expedido. Le permite gestionar obsolescencias.
Artículos Activos y sin Uso
Permite localizar los articulos que no han tenido movimientos desde una fecha determinada con la finalidad de saber en todo momento qué articulos tenemos y no usamos.
Proceso:
Acude a Consulta de Artículos Sin Movimiento.
Indica la fecha: ¿qué articulos no tienen movimiento desde esta fecha?,
Puedes realizar el filtrado por un artículo específico o bien por el estado en el que se encuentra (dato de la ficha del artículo).

Unidades de Medida (Doble Unidad)
Se ha de tener en cuenta que la aplicación facilita el tratamiento de los artículos en distintas unidades, de esta forma permite distinguir entre la unidad en la que compramos (unidad compra), la unidad en la que vendemos (unidad venta), la unidad que empleamos en fábrica al incorporar materia prima (Unidad fábrica) y la unidad en la que almacenamos (unidad interna) que será la considerada en la valoración de almacenes.
La unidad de compra, fábrica o venta se indica en cada ficha de artículo y puede indicarse también, a excepción de la unidad fábrica, en la relación artículo – cliente o artículo – proveedor para el tratamiento de aspectos especiales de estos. Sin embargo la unidad interna es única y se compara con el resto de unidades posibles, mediante un factor que representa la equivalencia entre ellas.
En conclusión:
Las distintas unidades (unidad A) se comparan con la unidad interna (unidad B) estableciendo sus equivalencias mediante el factor.
Para establecer las equivalencias tenemos 2 opciones:
Establecer equivalencias genéricas entre las unidades de medida que maneje en la aplicación. Para ello debe acudir a la pantalla ‘Mantenimiento de Conversiones Genéricas’.
Establecer otras equivalencias, no genéricas, sino particulares para determinado artículo. Para ello debe acudir a la ficha del artículo y configurar las equivalencias en su propia matriz de conversión.
Veamos un ejemplo: en una empresa comercializadora de agua, podemos tener que:
Compra Tanques de agua. Unidad Compra = Tanque (1000 lts.)
Almacena Litros de agua. UNIDAD INTERNA = Litro.
Vende botellas de agua. Unidad Venta = Botella (1,5 lts.)
Al cliente XX, vende en bidones de 5 lts.. Unidad Venta = Bidón (5 lts.)
En el ejemplo anterior, trabajamos con 4 unidades por lo que será necesario informar al sistema de sus equivalencias, que serán:
Unidad A = Tanque – Unidad B = litros – Factor = 1000.
Unidad A = Botella 1.5 lts. – Unidad B = litros – Factor = 1,5.
Unidad A = Bidón 5 lts. – Unidad B = litros – Factor = 5.

Factor de Conversión entre distintas unidades de medida
El sistema está preparado para la gestión de artículos en doble unidad esto es, en cada operación principal que realicemos podemos utilizar/consultar la información en dos unidades de medida distintas.
Se permite identificar hasta 4 unidades de medida distintas por artículo tomando como factor de conversión entre ellas el establecido en las Conversiones Genéricas o bien, estableciendo una conversión particular para un artículo determinado.
Conversiones Genéricas
Para poder realizar esta operación, es necesario que entre estas dos unidades de medida exista un factor de conversión. Este factor se puede establecer de forma genérica o bien de forma específica por Artículo.
Los factores de conversión genéricos se establecen en las Conversiones Genéricas.
Conversiones por Artículo
Por ejemplo: empresa embotelladora de agua. Vende en Botellas de 1.5 lts y en Bidones de distintos tipos ( 5 lts y 10 lts) siendo cada uno de estos envases una referencia distinta del catálogo de productos de venta, almacena en grandes depósitos de 1000 m3 de capacidad y compra en litros que va almacenando en estos depósitos.
La configuración de las Unidades sería distinta en función de las distintas referencias generadas a partir del análisis de la actividad de la empresa:
Unidad A = **Unidad de las operaciones (Venta, Compra o Fábrica).
Unidad B = *Unidad Interna (Almacén).
Factor = Valor que define cuántas Unidades A componen cada una de las Unidades B.
Consulta del stock en doble unidad
Para facilitar el acceso a la información el sistema incorpora la Consulta de doble unidad en la que puedes consultar las existencias en la unidad de medida que necesites analizar: ¿cuántas bolsas XXL (capacidad: 1000) puedo obtener de la referencia Tornillo R7 dadas las existencias del almacén central? por ejemplo.

Codificación Automática Avanzada
La codificación avanzada de artículos nos permite construir nuestra propia codificación a partir de cualquier dato contenido en la información del artículo.
Permite disponer de más de una codificación: códigos de materias primas, códigos de producto terminado, códigos para identificar determinados artículos, etc.
1. Configuración Previa
El uso de la codificación avanzada requiere no utilizar un Contador predeterminado asociado a la entidad: Artículos.
Proceso:
Acude a Contadores de Entidades.
Selecciona la entidad Artículo.
Comprueba que ninguno de los Contadores, que tiene asociados, tenga la opción ☑ Predeterminado activada.
2. Criterios de Codificación de Artículos
Crearemos la estructura (Código/Descripción) de nuestras codificaciones: ¿Cómo se construye el código/descripción? ¿Qué datos componen el código/descripción?. Podemos definir todas las codificaciones que deseemos: para productos terminados, para materias primas, etc.
Proceso:
Acude a Criterios de Codificación de Artículos.
Crea un nuevo criterio con la siguiente información:
Criterio de Codificación

Descripción Código
Contador: si lo deseamos podremos vincular nuestro código a un Contador de Entidad.
Código/Descripción
Campo: dato de la ficha del articulo usado para componer el código.
Entidad: origen de información (entidad/tabla) para componer la identificación.
Código: dato de la información de origen (entidad/tabla) que compondrá el código/descripción.
Característica: de forma alternativa al uso de la entidad como información de origen se puede utilizar las características del artículo. Util para el Configurador de Artículos, Producción o Bodegas, por ejemplo.
Orden: sirve para establecer el orden en el que se irá componiendo tanto el código como la descripción.

Configurar la codificación automática
Tipo-Familia del Artículo
La Codificación de Artículo creada requiere del Tipo y Familia para construir finalmente los códigos de artículo.
Proceso por Tipo:
Acude a Tipos de Artículos.
Indica en el Código la codificación que le corresponde.
Opcionalmente:
Código y Descripción abreviados: las abreviaturas son campos que permiten adoptar códigos y descripciones más sencillas que las habituales, podemos indicarlas opcionalmente.
Proceso por Familias: se permite establecer también la codificación a nivel de familia. Para esto, debemos indicar los datos del Código (o Código y Descripción abreviada) en cada línea de la familia.

Alta de un nuevo elemento codificado
Proceso:
Acude a Artículos y crea un nuevo registro.
Indica el Tipo y Familia.
Para obtener el código del artículo, pulsa sobre el botón Acceso a la codificación automática y avanzada de artículos .
Efectos:
Se propone el Código y/o la Descripción del artículo con los datos que hayamos configurado en el criterio de codificación: tipo, familia, la unidad, empresa, marca, etc.

Gestionar los Idiomas (traducciones del artículo)
Durante los procesos de gestión en los que interviene el artículo, el sistema le permite visualizar la descripción del artículo en el idioma del cliente  / proveedor, dato que se muestra en los campos de referencias. Para entender mejor la funcionalidad, y los datos que debe registrar para obtener esta traducción, se indican a continuación los pasos que da el sistema para gestionar los idiomas.
Primer dato: idioma del cliente / proveedor.
El sistema identifica este dato en la Ficha Cliente / Proveedor >> Datos de Identificación.  Ejemplo: un cliente tiene asociado el idioma ING - inglés.
Segundo dato: la traducción (idioma y descripción idioma).
El sistema acude a la solapa idiomas del mantenimiento del artículo y comprueba de entre todas las traducciones ahí localizadas si alguna corresponde al idioma del cliente o proveedor. Ejemplo: vemos en la ficha del artículo ‘AR00000168 - Camisa Tudor' > solapa idiomas, está asociada la traducción al idioma del Cliente (Ingles): 'ING - Shirt’.
Tercer dato (resultado): la referencia del cliente / proveedor.
Una vez comprobado que el cliente / proveedor en efecto tiene asociada una traducción para su idioma, el sistema muestra esta traducción en el apartado ‘Descripción Referencia Cliente / Proveedor’ del proceso que se esté gestionando (factura, albarán, pedido, etc.). Ejemplo: descripción del artículo = ‘Camisa’, y descripción referencia cliente = ‘Shirt’.
Nota: este proceso se realiza siempre y cuando en la ficha del cliente / proveedor no exista una referencia para el artículo (ficha cliente / proveedor  >  solapa ‘Artículos’  > campo ‘Descripción Referencia Cliente’ / ‘Descripción Referencia Proveedor), de ser así se muestra esta referencia.

Gestión de Tallas y Colores
En ocasiones se va a encontrar con la necesidad de generar referencias que parten de un mismo elemento, caso de la gestión de Tallas y Colores en el ámbito TPV por ejemplo. Para explicar cómo gestionar estas referencias veamos un ejemplo: tenemos el artículo ‘Pantalla PC LCD modelo ZK10’ en distintos tamaños: 14’’, 18’’, 20’’ y 22’’. De forma que tenemos un artículo pero realmente necesitamos inventariar una ficha de artículo por cada una de las referencias, ya que tanto el aprovisionamiento, como el control del stock como el proceso de venta necesita identificar la referencia concreta.
Las pantallas implicadas en esta gestión son:
Características de Artículo: para inventariar los valores de las características cuyo alcance incide tanto en la gestión de sus aprovisionamientos como en el control de gestión y por supuesto, en sus ventas. Se pueden utilizar un máximo de 5 características por cada Familia de artículos (por ejemplo: capacidad hd,pulgadas pantalla, talla, color, tejido, etc.…).
Tipos de Artículos: en la que configurará la relación entre los tipos-familias y las características que se van a manejar.
Artículos: en la que registrará el artículo de origen, ‘Pantalla PC LCD modelo ZK10’ por ejemplo, junto a todas sus especificaciones (cuentas contables, unidades, proveedores habituales, clientes habituales, condiciones económicas especiales, etc.) y posteriormente mediante un sencillo proceso, conseguirá crear en un solo paso tantas referencias (fichas de artículos ‘hijo’) como variables haya configurado.

Configurar las Características
El sistema permite trabajar con un máximo 5 características.
Acude a Características de Artículo.
Selecciona la Característica: 1-5.
Indica los Valores asociados a la Caracterísitica seleccionada.
Debes tener en cuenta que los códigos formarán parte del código de los artículos que vamos a obtener y la descripción del valor pasará a la descripción del artículo.
Ejemplo:
Configuración de las Tallas: utilizaremos la Característica 1
Caracterísitica: 1 (para las Tallas)
Característica ID-1 / Caracterísitica 1
S / Talla S
M / Talla M
L / Talla L
XL / Talla XL
Caracterísitica: 2 (para los Colores)
Característica ID-2 / Caracterísitica 2
BL / Blanco
NG / Negro
AZ / Azul
RJ / Rojo
VD / Verde
Ejemplo:
El artículo "Abrigo modelo Winter" con código ABR002, tras ejecutar el proceso de generación de artículos obtendremos el siguiente código y descripción:
El artículo ‘Pantalla PC LCD modelo ZK10’ tiene el código = PLCD003, tras ejecutar el proceso de generación de artículos obtendrá por ejemplo para el modelo de 14’’ el siguiente código y descripción: PLCD003_14 y ‘Pantalla PC LCD modelo ZK10 14’’ ’.

Asociar las características a las Familias
Proceso:
Accede a Tipos de Artículos.
Selecciona el Tipo de Artículo. Por ejemplo: Prendas de vestir.
Sitúate sobre la línea de la Familia y activa las opciones de las Características a gestionar.
Siguiendo con nuestro ejemplo: activaremos las ☑ Característica 1 y ☑ Característica 2, dado que hemos configurado la C1 para las Tallas y la C2 para los Colores.

Generar artículos a partir de una referencia común
Referencia ‘Padre’:
En primer lugar necesitamos crear la ficha del artículo a partir del cual generaremos las referencias en las que aplicaremos las características configuradas.
Daremos de alta un nuevo artículo que representa el artículo ‘padre’ en nuestro caso: PLCD003 | Pantalla PC LCD modelo ZK10.
Generar referencias ‘hijo’:
Una vez registrados los artículos procede a generar los nuevos artículos según sus características, para ello:
Acceda a la ficha del artículo ‘padre’.
Ejecuta el proceso Procesos Solmicro ERP Generar Artículos Características.
El sistema muestra el listado de valores correspondientes a las características que se han activado en la ficha del tipo-familia al que pertenece el artículo.
Activa las opciones de los valores que interese. En nuestro caso, solo activaremos las marcas de la característica que identifica el tamaño de la pantalla (14, 18, 20 y 22).
Procede a lanzar el proceso, pulsando en el botón  Generar Artículos.
El sistema mostrará una propuesta de tantas referencias como combinaciones puedan darse según los valores seleccionados.
El código propuesto se crea a partir del código del artículo padre añadiéndole el código de las variables que han participado. Siguiendo con el ejemplo planteado, se proponen los códigos: PLCD003_14, PLCD003_18, PLCD003_20 y PLCD003_22.
La descripción propuesta se crea a partir de la descripción del artículo padre añadiéndole el texto descriptivo de las variables utilizadas, según el ejemplo se propone: Pantalla PC LCD modelo ZK10_14’’, etc.
Selecciona de los artículos pre-generados los que deseas registrar ya que puede ocurrir que alguna de las combinaciones obtenidas no vaya a ser gestionada y por lo tanto no interese crear la correspondiente ficha de artículo.
Como último paso, el sistema muestra el cuadro de diálogo ‘Generar Artículos nuevos’ donde se muestra agrupada (según solapas de datos) la información de la ficha del artículo ‘padre’: unidades, clientes, proveedores, etc. Puedes desactivar las opciones de los conceptos que no interese trasladar a las fichas de los artículos ‘hijo’.
Código y Descripción
El código propuesto se crea a partir del código del artículo padre añadiéndole el código de las variables que han participado. Siguiendo con el ejemplo planteado, se proponen los códigos: PLCD003_14, PLCD003_18, PLCD003_20 y PLCD003_22.
La descripción propuesta se crea a partir de la descripción del artículo padre añadiéndole el texto descriptivo de las variables utilizadas, según el ejemplo se propone: Pantalla PC LCD modelo ZK10_14’’, etc.
En el apartado Características (apartado: Características Artículos) puedes visualizar las características y valores del artículo activo así como del artículo ’padre’ a partir del que se ha generado. Posteriormente puedes utilizar estos valores en la búsqueda de artículos, de gran utilidad en determinados ámbitos como puede ser el TPV donde se necesita acceder rápidamente a la consulta de referencias en función de sus propiedades.

Parametrizar la Producción
Permite identificar cómo realizamos el descuento de materiales y las entradas de producto terminado resultante del proceso de fabricación.
Acude a Artículos.
Localiza el artículo y ejecuta el proceso  Parametrizar la Producción.
Las opciones son:
Salida de Materia Prima
Primera operación a control
Última operación a control
Operación en estructura
Vale de Material
OF Completa
Entrada de Producto Terminado
Última operación a control
OF Completa

Coste del Artículo (estándar/último)
Este proceso permite acceder a la información de Coste Estándar, tanto con los datos del Coste Último como del Coste Estándar.
Permite realizar cálculos y almacenar el último Coste obtenido del proceso de fabricación realizado con un artículo considerando su estructura de componentes así como las operaciones de su ruta de fabricación. Mediante la comparación del último Coste Estándar fijado con el resultado obtenido del cálculo del último coste, puedes advertir desviaciones así como actualizar el Precio Estándar del artículo objeto de análisis.
Se almacena un histórico con las fechas de cálculo de forma que puedes recuperar información obtenida y operar con ella.
Acude a Artículos
Localiza el artículo y ejecuta el proceso  Ir a Ficha Coste.

Estructura Multinivel (Rutas y Estructuras)
Los datos de las Rutas y Estructuras del artículo están agrupados en distintos apartados lo que permite un acceso multinivel a la información así como realizar acciones de forma agrupada. Solmicro ERP incorpora una pantalla en la que se puede consultar y manejar esta información de forma gráfica e intuitiva.
Acude a Artículos
Localiza el artículo y ejecuta el proceso  Ver Estructura Multinivel.
La pantalla está dividida las siguientes áreas:
En la zona superior, se muestran los datos del artículo desde el que hemos accedido (Código y Descripción).
En la zona izquierda, se muestran los árboles de Estructuras y Rutas.
En la zona derecha, se muestran los siguientes apartados:
Detalles: muestra el detalle de Estructura y Rutas de los elementos seleccionados en los árboles de Estructuras / Rutas.
Copiar Estructuras: permite traer las estructuras de un artículo origen, y copiar sus elementos individualmente al artículo de cabecera.
Implosión Artículo: permite saber en qué artículos se encuentra como componente un artículo.
Copiar Rutas: permite traer las rutas de un artículo origen y copiar sus elementos individualmente al artículo de cabecera. Sustituir Componente: permite sustituir un componente por otro en uno o varios artículos.
Consulta multinivel
Por defecto se muestra una visión centralizada de las Rutas y de las Estructuras planteada de forma gráfica e intuitiva. La herramienta permite consultar, por ejemplo, qué otros artículos utilizan los componentes del artículo consultado incluso cuando el artículo consultado es, a su vez, un componente.
Acciones multinivel
Permite realizar acciones para modificar la estructura o ruta de uno o varios artículos a la vez.

Gestionar Artículos de forma gráfica
Permite ver la Estructura de un artículo de forma gráfica pudiendo acceder a consultas y procesos de sus componentes.
Se utiliza en artículos con estructura, de tipo Fábrica o Kit.
Acude a Artículos.
Localiza el artículo a consultar.
Ejecuta el proceso  Ver Estructura Gráfica.
El sistema muestra el diagrama con el color asociado al Tipo de artículo / componente y sobre las líneas del diagrama (x1, x2, xN…), representan la cantidad de componentes que se requieren para fabricar el artículo inmediatamente superior.

Operaciones
Para acceder a las operaciones de consulta y otros procesos, pulsamos con el botón secundario en cualquiera de los elementos.
Consultas referentes al artículo
Ver Artículo: acceso a la ficha del artículo del elemento seleccionado.
Disponibilidad: acceso a la Consulta de Disponibilidad: pedidos de compra, pedidos de venta, artículos en curso, existencia de números de serie, etc...
Consultas referentes a las ventas
Pedido de Venta: acceso a la Consulta de pedidos de venta.
Albarán de Venta: acceso a Albaranes de venta detallados.
Factura de Venta: acceso a Facturas de venta detallados.
Consultas referentes a las compras
Pedido de Compra: acceso a la Consulta de pedidos de compra.
Albarán de Compra: acceso a Albaranes de compra detallados.
Factura de Compra: acceso a Facturas de compra detallada.
Consultas referentes a la fabricación
Ordenes de Fabricación: le permite acceder a la pantalla de Control de situación de la fábrica, desde la que:
Podremos obtener la hoja de ruta de fabricación del artículo mediante los informes asociados a la ficha (botón de impresora).
Podrá realizar modificaciones en las ordenes de fabricación, tales como modificar la ruta y la estructura.
Podrá consultar las necesidades de compra de materiales así como la de semielaborados.
Consultas referentes a la Gestión de Calidad
Pauta de Control Final: le permite acceder a la pantalla “Pautas de Control Final”, la cual contiene los controles de calidad que se realizan al producto terminado
Pauta de Proceso: le permite acceder a la pantalla “Pautas de Control de Proceso” la cual muestra los controles de calidad para los artículos semielaborados que tendremos en cuenta durante la fabricación de un artículo.
Pauta de Recepción: le permite acceder a la pantalla “Pautas de Control de Recepción” que integra los controles de calidad para los artículos que tendremos en cuenta durante la recepción de compra en general.

Gestión del Precio Estándar
El precio estándar de las existencias nos indica un precio previsto, o bien un precio de adquisición o fabricación. Su estimación es trabajo de nosotros mismos y se basa en datos provisionales o bien de constante cambio. Es muy útil para el control de nuestra empresa ya que mediante una comparación con el precio real podremos desviar desviaciones sobre los objetivos establecidos.

Actualizar los Precios Estándar
El sistema nos permite consultar, visualizar y modificar el precio estándar de nuestros artículos de forma masiva. Para ello habilita  la pantalla de “Actualización de Precios estándar”. Al ser una Consulta Interactiva, podremos utilizar sus características para obtener información referente al precio estándar, generar informes y guardar vistas. El principal cometido de esta pantalla sin embargo, es el de actualizar el precio estándar de nuestros artículos de forma masiva, para ello:
Una vez marcadas las líneas a actualizar selecciona una de las siguientes operaciones:
Modificando de forma manual: al seleccionar esta opción el sistema habilita el campo ‘Nuevo Precio’ localizado en cada una de las líneas de artículos, en este campo puede introducir el nuevo precio estándar para cada artículo.
Aplicando un porcentaje sobre el precio estándar actual: al seleccionar esta opción el sistema muestra el campo ‘Porcentaje’, en este campo puede establecer el porcentaje que se va a aplicar sobre el precio estándar actual.
Aplicando un porcentaje sobre el precio último: al seleccionar esta opción el sistema muestra el campo ‘Porcentaje’, en este campo puede establecer el porcentaje que se va a aplicar sobre el precio último de compra.
Igualando el precio estándar al precio último: indica que el nuevo precio estándar ha de ser igual al precio último existente.
Ejecuta el proceso  Actualizar Precios.

Actualización de las Ventas con el último Precio Estándar
Se trata de otro programa para el cálculo del precio estándar. Mediante esta accíón podemos cambiar el precio de coste de las ventas (líneas de Pedido/Albarán/Factura de venta) a partir de una fecha indicada.
Antes de ver el proceso debemos tener en cuenta que la acción solo aplica a artículos cuyo criterio de valoración del artículo sea Precio Estándar, por lo que los artículos a actualizar deben tener la configuración: Solapa Almacenes à  Criterio de Valoración: Precio Estándar.
Acude a Actualizar Ventas con Ultimo Precio Estándar, localizamos y seleccionamos los artículos que vamos a actualizar.
Indica la Fecha a partir de la cual cambiaremos el precio de coste de las ventas.
Ejecuta el proceso Actualizar Precio Estándar.
El precio de coste de las ventas se ha modificado, así como todos los movimientos del histórico de movimientos, posterior a esa fecha.

Actualizar los Plazos de Compra / Fábrica
Este proceso atañe tanto al circuito de compras como al de fabricación; permite modificar el plazo necesario para comprar o fabricar un artículo.
Acude a Actualización de Plazos de Artículos.
Operación: este campo contiene una serie de operaciones que nos facilitarán la imputación del nuevo plazo.
Modificando de forma manual. Permite indicar manualmente un nuevo plazo de compra o fábrica para cada artículo:
Seleccionamos esta operación.
Seleccionamos las líneas a modificar
Indicas el nuevo Plazo para cada línea.
Ejecutamos el proceso  Actualizar el Precio de Compra o bien Actualizar el Precio de Fábrica.
Para actualizar el precio compra la marca “compra” debe estar activa.
Para actualizar el precio de fábrica la marca “fábrica” debe estar activa.
Las marcas corresponden al alcance funcional indicado en la ficha del tipo de artículo de cada material.
Aplicar un valor. Permite aplicar el mismo plazo a todos los artículos seleccionados.
Seleccionamos esta operación.
Se mostrará el campo “Plazo” debajo del campo de operación, en este indicaremos el plazo que se aplicará a todos los artículos seleccionados.
Seleccionamos las líneas a modificar.
Ejecutamos el proceso  Actualizar el Precio de Compra o bien Actualizar el Precio de Fábrica.
Para actualizar el precio compra la opción “Compra” debe estar activa.
Para actualizar el precio de fábrica la opción “Fábrica” debe estar activa.
Las marcas corresponden al alcance funcional indicado en la ficha del tipo de artículo de cada material.
Calcular el plazo de compra: el sistema calcula e imputa de forma automática el plazo de compra, teniendo en cuenta los datos de las entregas del proveedor.
Seleccionamos esta operación.
Seleccionamos las líneas a modificar.
Ejecutamos el proceso  Actualizar el Precio de Compra.
Para actualizar el precio compra la marca “compra” debe estar activa.
La marca corresponde al alcance funcional indicado en la ficha del tipo de artículo de cada material.
Calcular el plazo de fábrica (tiempos, capacidad, lote): el sistema calcula de forma automática el plazo de fabricación del artículo teniendo en cuenta todos los datos que intervienen en su fabricación.
Seleccionamos esta operación.
Seleccionamos las líneas a modificar.
Ejecutamos el proceso  Actualizar el Precio de Fábrica.
Para actualizar el precio fábrica la marca “fábrica” debe estar activa.
La marca corresponde al alcance funcional indicado en la ficha del tipo de artículo de cada material.

Registro y Configuración de Almacenes
La primera operación que debe realizar es registrar sus almacenes; la aplicación le permite gestionar tantos almacenes como necesite. Este proceso se realizará desde el Mantenimiento de Almacenes.

Crear los almacenes
Acude a Almacenes, inicia un nuevo registro. La información obligatoria es: Código y Descripción.
Selecciona la opción ☑ Activo para permitir las recepciones y las expediciones de mercancía.
Selecciona la opción ☑ Empresa para considerar este almacén en el proceso de Valoración de Almacenes.
Indica el Centro de Gestión asociado al almacén y selecciona la opción Principal para destacarlo sobre otros almacenes del mismo centro de gestión.
 Ubicaciones del almacén. Este proceso afecta a la gestión de lotes – ubicación. En el siguiente proceso veremos cómo se realiza el registro de una ubicación.

Ubicaciones de almacén
Acude a Almacenes y localiza el Almacén en el que se van a identificar las Ubicaciones.
Accede a las Ubicaciones a través del botón .
Puedes inventariar el listado de ubicaciones asociado al almacén seleccionado: Pasillo A, Pasillo Central, Pasillo A - Balda1, etc.
Indica una ubicación como Predeterminada que será la que propone el sistema proponga en determinados procesos como, por ejemplo, en la recepción de un Lote de artículos.
Ubicación predeterminada
Por defecto, siempre existe una ubicación configurada previamente en los parámetros generales de la aplicación (Ubicación asociada al lote |UBIC_NODEF|).

Almacenes de Depósito (Consigna)
Utilizados en la gestión de la mercancía en depósito del circuito de Ventas. Debemos crear un almacén para identificar el origen de los consumos del cliente. Estos consumos serán el origen de la facturacion al cliente.
En mercados como el de la automoción el fabricante solicita disponer de un stock de seguridad por ejemplo, para los repuestos. En este caso se realiza la expedición del stock, pero se acuerda realizar la facturación conforme se vaya consumiendo de este almacén ‘intermedio’ (también denominados ‘almacenes de consigna’), por lo que el origen de la facturación no es el envío inicial sino estos consumos.
A tener en cuenta:
El envío inicial al almacén de depósito no genera facturación sino que serán los consumos posteriores los que indiquen qué mercancía se va a facturar.
La mercancía se ubica en el almacén de depósito hasta que el cliente solicite el consumo de determinado número de piezas. De esta forma el verdadero propietario de la mercancía somos nosotros ya que el cliente todavía no la ha pagado y la pagará conforme vaya haciendo consumos de ella.
Cada vez que el cliente haga uso de esta mercancía deberá notificarnos este hecho para que procedamos a su facturación y, en este momento, el material deberá ser dado de baja en el Almacén de Depósito.
Información del Almacén de Depósito en el registro de almacenes:
Depósito.
Empresa: indica que las existencias son nuestras y por ello deben tratarse en la Valoración de almacenes y/o en los Cierres contables de almacén (Inventario).


Almacén de Depósito asociado al Cliente
Para asociar el almacén al cliente e identificar el destino de la mercancía inicial utilizamos las direcciones de envío al cliente seleccionando una de ellas como la correspondiente al Almacén de Depósito.
Acude a Clientes, apartado Direcciones.
Crea o localiza la dirección que identifica la ubicación del almacén e indica su código en el dato Almacén de Consigna.


Almacenes Envases Retornables
Utilizados en la Gestión de Envases Retornables en la que "necesitamos" un almacén, ficticio o real ("casa del cliente") para por un lado, valorar los envases de nuestra propiedad y por otro, utilizar el dato del almacén como origen en la devolución de los envases retornables.
Información del Almacén de Envases en el registro de almacenes:
Empresa: indica que las existencias son nuestras y por ello deben tratarse en la Valoración de almacenes y/o en los Cierres contables de almacén (Inventario).


Almacén de Envases
Para asociar el almacén al cliente e identificar el destino de la mercancía inicial utilizamos las direcciones de envío al cliente seleccionando una de ellas como la correspondiente al Almacén de Depósito.
Acude a Clientes, apartado Direcciones.
Crea o localiza la dirección que identifica la ubicación del almacén e indica su código en el dato Almacén Contenedor.
Ver Gestión de Envases Retornables

Asignar un Almacén predeterminado
Este proceso se realiza mediante los parámetros de la aplicación. Nos permite asignar un almacén por defecto a los artículos que se vayan registrando (solapa Almacenes).
Para establecer un almacén predeterminado:
Acudimos a Parámetros. Localizamos el parámetro: ALM_PREDET | Almacén Predeterminado.
Indica el código del Almacén que desesa establecer como predeterminado.

Almacén por Centro de Gestión o por Artículo: asignación automática (circuito)
Como hemos visto, podemos asignar un almacen tanto a nuestros centros de gestión (ficha de almacenes “Centros de Gestión” y “Principal”) como a nuestros artículos (solapa almacenes).
Al producirse un movimiento de stock de entrada o salida, podremos determinar si el material va a sumarse o restarse de el almacén del artículo o bien el del centro de gestión. Son distintas posibilidades de enfocar su gestión, le recomendamos realice el correspondiente análisis que le permita decidir cuál de las opciones le sería más favorable en su negocio.
Acudimos a Parámetros. Localizamos el parámetro: Gestión de almacenes por Centro de Gestión (ALMCC):
Seleccionamos el valor correspondiente a la opción que vayamos a requerir:
Sí: Los movimientos de stock por defecto manejarán el almacén asociado al centro de gestión vinculado al proceso (pedido, albarán, factura, etc.) antes que el almacén vinculado al artículo.
No: Los movimientos de stock siempre manejarán, por defecto, el almacén asociado al artículo.
El orden de asignación será:
Si valor es Sí: el sistema acudirá al Centro de Gestión asociado al proceso de expedición / recepción, recogerá el almacén principal del centro de gestión y lo asociará a las líneas del proceso E / S.
Si valor es no: el sistema recogerá el almacén predeterminado de la referencia (artículo) que pretenda recibir / expedir.
Si el artículo no tiene información de almacén (debido a una carga inicial de datos incompleta, por ejemplo) el sistema recogerá el almacén predeterminado en parámetros.
Excepción: en la gestión de albaranes de consigna o depósito en la que el sistema utilizará el almacén de envío asociado a la dirección del cliente.

Configuración de Artículos con gestión de stocks
En este apartado se detallan los aspectos a tener en cuenta al registrar un artículo que utilizará la gestión del stock.

Tipos de Artículos
Importante: el sistema utiliza el dato del Tipo de Artículo para trasladar la información inicial necesaria en el registro de Artículos con gestión de stock.
Para poder gestionar el stock, el Artículo ha de tener asociado un Tipo de artículo que tenga activada la marca ☑ Gestión de Stocks.
Indicaremos los Criterios de valoración de almacenes a nivel de Tipo de artículo. Esta información se trasladará a la ficha del Artículo, apartado Almacenes, al que se asocie dicho Tipo de Artículo. Si se desea, se pueden actualizar los criterios de valoración a nivel de artículo.
Recalcular Valoración en Movimientos de Salida: cuando exista un movimiento de salida de un almacén, determinaremos si recalculamos precios o mantenemos el precio de salida.
Criterio de Valoración: indicamos cuál es el criterio empleado para valorar las existencias: FIFO, LIFO, Precio Estándar, Precio Última compra, etc.
Para la contabilización del proceso de Regularización de Existencias podemos asociar a las Familias del Tipo de Artículo la cuenta contable a utilizar. Esta cuenta contable la heredan los artículos a los que se asocia el Tipo-Familia de Artículos. Puedes ver este dato en el apartado Almacenes de la información del Artículo.

Artículos
Información del Artículo vinculada con la gestión del stock:
Información del Artículo
Activo: opción que si está desactivada impide las entradas o salidas de stock.
Cuenta Contable Stock: necesaria para la Regularización de Existencias e Inventario Permanente. (Apartado Cuentas Contables)
Almacenes
Almacenes: listado de Almacenes en los que puede ubicarse el Artículo. Existirá un almacén predeterminado.
Stock Negativo: permite realizar movimientos con stock negativo.
Lotes-Ubicación: 1 Lote: N Artículos. Ejemplo: los artículos resultantes de cada orden de fabricación llevan asociados un número de lote donde se indica la OF que los ha originado junto a la fecha y hora de fabricación, este número identificador es común para todos los productos obtenidos en la OF.
Nº de Serie: 1 Nº Serie = 1 Artículo. Ejemplo: empresa de Alquiler de Vehículos. Su artículo central es el vehículo, donde cada registro del mantenimiento de artículos identifica a un modelo de ellos pero resultará imprescindible identificar de forma inequívoca cada una de las unidades de un mismo artículo, es decir, tenemos en el parque 5 automóviles del tipo “x” (modelo, marca, cc, etc) para identificarlos tenemos una ficha de artículo donde se dice que hay 5 unidades, utilizaremos los números de serie para identificarlos de forma individual y cada número de serie se identificará con el número de matrícula de cada unidad. Cada vez que realicemos un movimiento de stock, el sistema solicitará el correspondiente número de serie.
Recalcular Valoración en Salidas: este dato se hereda del tipo de Artículo, aunque puede ser modificado. Indica cómo se realizará la valoración del stock al momento de su salida. Es un dato que utilizaremos si gestionamos el Stock del artículo, para el cálculo de la Valoración de Almacenes.
Mantener precios de salida: en los movimientos de salida (expedición) se mantendrá el precio del Albarán correspondiente.
No recalcular: en los movimientos de salida (expedición) se propone el precio asociado al criterio de valoración del artículo activo.
Recalcular: en los movimientos de salida (expedición), en el caso de que el criterio de valoración sean FIFO o Medio, la aplicación recalculará el precio en el momento.
Criterio de Valoración: este dato se hereda del tipo de Artículo, aunque puede ser modificado. Indica el Criterio que se utilizará para realizar la valoración del almacén. Es un dato que utilizaremos si gestionamos el Stock del artículo, para el cálculo de Valoración de almacenes.
Precio Estándar, Precio FIFO (ordenado por fecha documento), Precio FIFO (ordenado por fecha movimiento), Precio Medio, Precio Última Compra.
Por defecto, el sistema propone el criterio de valoración asociados al Tipo del Artículo.
Unidades / Precios
Unidad Interna
Precio Estándar
Precio Última Compra
Estructura
Si la referencia se corresponde con un artículo de tipo Kit se deben indicar los artículos que componen el Kit y en qué cantidades.
Costes / Producción
Selecciona la opción ☑ Aplicar Lote MRP si requieres considerar el dato de Lote mínimo a la hora de calcular los plazos y cantidades en la Planificación MRP de Fabricación o de Compra. El dato Lote Mínimo se establece en el Artículo para cada uno de los almacenes en los que pueda estar ubicado.
Calidad
Existe un control que puede afectar al stock, éste es el Estado de Homologación asociado al artículo que debe permitir que se pueda expedir. Se informa del estado en el campo ‘Estado de homologación’ mostrado en la solapa Calidad, de la ficha del artículo activo. En los Estados de Homologación se asocia a cada uno de los estados la característica de Expedible. De este modo la homologación de un artículo incidirá en su posible expedición o no.

Configuración de los Tipos de movimientos en el almacén
Los movimientos de stock representan las entradas, salidas e inventarios de material, tienen su origen en la necesidad de atender un pedido de un cliente, incorporar determinado material en un proceso productivo, comprar un tipo de suministro para la oficina, inventarios periódicos, etc.
Cada vez que realicemos un proceso que requiera una entrada, salida o inventario de material, el sistema actualizará la información de los almacenes de forma que las existencias estén siempre controladas.
Este proceso de control, aunque lo veremos mas adelante, deberemos entender que existe ya que en este apartado tendremos que realizar el registro que le precede.
Antes de poder realizar un movimiento, deberemos decirle al sistema qué movimientos podemos tener, es decir los mencionados anteriormente: recepciones de albaranes, expediciones a cliente, inventarios, etc.
En esta pantalla se detallan los tipos de movimiento que posteriormente serán asociados en las entradas y salidas de stock.
Tipo Movimiento: código que identifica el tipo de movimiento.
Descripción Tipo Movimiento: texto descriptivo asociado al código anteriormente insertado.
Código Tipo Movimiento: abreviatura asociada al tipo de movimiento.
Clase Movimiento: identificador de la clase de movimiento, donde:
0: movimientos de inventario.
1: movimientos de salida de stock = resta stock. (Output)
2: movimientos de entrada de stock = suma stock. (Input)
3: movimientos de corrección.
☑ FIFO: movimientos que intervienen en el cálculo del precio FIFO.
☑ Consumo: movimiento aplicado en los consumos originados en fábrica (salida materia prima).
☑ Manual: movimientos que pueden ser realizados manualmente a través del programa “Movimientos de Stock”.
☑ Sistema: información crítica. La aplicación informa de los tipos de movimientos necesarios e imprescindibles para la correcta evaluación de los movimientos de entrada y salida. Estos registros no deben ser modificados por el usuario ya que se necesitan en los procesos automáticos realizados por la aplicación.

Control de Almacén
Para controlar las existencais en nuestro almacen tendremos en cuenta dos conceptos:
los Movimientos de Stock y
la Actualización de Stock.
En esta introducción veremos el proceso global de control de almacen, más adelante detallaremos los procesos a los que se hacen referencia.

Movimiento de Stock
El movimiento de stock es el proceso que registra los movimientos de material, si recordamos los procesos anteriores, tenemos que los movimientos de stock pueden ser de varios tipos: salidas, entradas, inventarios, etc. Cada uno de ellos registra un aumento o disminución de nuestras existencias.

Actualización de Stock
La actualización de stock es el proceso que desencadena el movimiento, es decir, es el proceso que indica al sistema que se ha realizado un movimiento y las condiciones de dicho movimiento.

Origen del movimiento
La orden para realizar la actualización y el movimiento de stock se origina en las necesidades de consumo, expedición o recepción de material representadas en la aplicación con las fichas de albaranes de compra o venta, procesos de entrada de producto terminado en fábrica, consumos de material en fábrica o proyectos, etc.
El envío de la orden de actualización o movimiento de stock puede ser manual o bien automática, dependiendo de cómo configuremos nuestra aplicación.

Ejemplo: "Atender un pedido de un Cliente"
En el departamento de ventas recibimos la solicitud compra de mercancía de un Cliente, por lo que registramos un Pedido de Venta en la aplicación. En el pedido indicamos las cantidades, precios de las referencias, así como los datos del Cliente.
Posteriormente se confirma el pedido, otro proceso del circuito de ventas, con esta confirmación entendemos que podemos proceder a enviar el producto al Cliente, es decir realizar la Expedición de la Venta.
En el momento de realizar la expedición se genera el albarán de venta. El albarán de venta como hemos dicho, está vinculado a la gestión de stock y es el que desencadena el proceso de actualización y movimiento de stock. En este punto, para el caso de las ventas y las compras, se abren dos vertientes.
Dependiendo de cómo hayamos configurado la aplicación la actualización puede ser de dos formas:
Actualización automática: si tenemos parametrizado este automatismo, al momento en que se expida la mercancía y se crea el albarán, el sistema lanza actualización de stock automáticamente, únicamente informa de la realización del proceso mediante una pantalla. Si a partir de ese momento revisamos el histórico de movimientos, veremos que se ha generado igualmente el registro correspondiente a la expedición del material.
Actualización manual: en este caso el parámetro de actualización de stock indica que se realiza manualmente. Al momento de expedir la mercancía, se crea el albarán. El sistema recoge esta información y la registra como una en una pantalla cuya finalidad es permitirnos actualizar el stock de los albaranes generados. Hasta este punto el almacén no está actualizado: no se muestran movimientos en el histórico de movimientos ni se refleja la nueva cantidad de artículo en almacén. La persona responsable de realizar la actualización, deberá acceder a dicha pantalla y ejecutar manualmente el proceso de “Actualización de Stock”.
Las pantallas de Actualización de Stock manual sirven también en caso de que una actualización automática no haya podido realizarse por algún motivo (no hay stock suficiente, no se ha indicado un lote, etc.).
Existe pantallas de Actualización de Stock manual para todos los procesos afectados: ventas compras, fábrica, proyectos...
Existen pantallas que le permitirán actualizar únicamente líneas específicas del albarán.
Antes de ver los procesos de control de stock, tendremos los siguientes aspectos de la aplicación:
Estado de Artículo: si la opción ☑ Activo está desactivada (el artículo no está activo), no se permiten ni entradas ni salidas de stock.
Estado de Homologación: el estado de homologación de un artículo se indica en la solapa de Calidad de la ficha del artículo. Controla la expedición/salida de almacén de un artículo.
Almacén:
Activo: en caso de estar desactivado, no se permiten ni entradas ni salidas de mercancía.
Bloqueado: si el valor asociado es positivo, sólo se permitirán realizar transferencias y movimientos de entrada a este almacén, no se permiten realizar salidas de mercancía.
Lote:
Bloqueado: el sistema controlará que no se puedan realizar expediciones para este lote. Puede gestionar esta marca en la pantalla Consulta de Lotes.

Actualización del stock
Actualización del stock La actualización de stock es el proceso mediante el que la aplicación desencadena el movimiento de stock, es decir, es el proceso que indica al sistema que se ha realizado un movimiento y las condiciones de dicho movimiento.
Parametrización:
Compras
Actualización automática del stock vinculada al Albarán de Compra (Parámetro: AUTACT_ALC):
1 | Verdadero: la actualización es automática, se realiza a la vez que el registro del albarán de compra.
0| Falso: la actualización de forma manual. Para actualizar el stock deberá utilizar los programas de Actualización de Stocks en las Compras.
Ventas
Actualización automática del stock vinculada al Albarán de Venta(Parámetro: AUTACT_ALV). 1 | Verdadero: la actualización es automática, se realiza a la vez que el registro del albarán de venta. 0| Falso: la actualización de forma manual. Para actualizar el stock deberá utilizar los programas de Actualización de Stocks en las Compras.
Producción
Si utiliza el módulo de producción, deberá parametrizar en qué momento se va a realizar la actualización de stock del producto terminado (entrada) y consumo de materia prima (salida).
Actualización de Stock en las Ventas
Actualización de Stock en las Compras
Actualización de Stock en la Producción
Actualización de Stocks en los Proyectos
Actualización de Stocks en GMAO

Movimientos de stock
El movimiento de stock es el proceso que registra los movimientos de material.
Puede haber varios tipos de Movimientos dependiendo de qué proceso genera el movimiento; estos se han registrado previamente en Tipos de Movimientos.
Los movimientos se registran automáticamente al actualizar el stock desde albaranes de venta, compra, consumos, etc.
Pueden existir otros movimientos manuales propios de la actividad de la empresa, podemos realizar movimientos de ajuste o corrección y finalmente podemos revisar el histórico de todos los movimientos que se hayan realizado en nuestros almacenes.

Contador de Movimientos
Debemos dar de alta el contador que se utilizará para numerar todos los movimientos de stock, por lo tango debemos crear el contador para numerar los Movimientos de Stock.
Acude a Parámetros.
Localiza el parámetro: HIST_MOV | Movimientos de Stock: Contador.
En el dato Valor, Indica el código del Contador previamente generado.
"""
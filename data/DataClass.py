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
Los procesos del circuito de Stocks se refieren a los procesos básicos de la gestión:
Realizar los Inventarios.
Controlar nuestros Almacenes.
Por un lado podremos realizar la entrada y salida de material. Este proceso se realiza durante los procesos de recepción en compras y expedición en ventas, o bien desde la fabricación, con el control de consumibles y materia prima, así como los productos terminados.
Generar movimientos que no se encuentren vinculados a ningun proceso gestionable. Realizar ajustes, transferencias, y llevar un histórico de todos los movimientos realizados.
Valorar los almacenes. Proceso con el que podremos saber siempre el valor de nuestros almacenes, tanto el valor actual como el valor de una fecha determinada. Igualmente podremos utilizar cualquiera de los criterios de valoración de almacén: FIFO, LIFO, Última Compra, Precio Estándar y Precio Medio.
Finalmente se realiza el Cierre del Inventario obteniendo la información contable para el posterior paso, la Regularización de Existencias en el módulo de contabilidad.
La Gestión de Stocks incorpora una serie de herramientas que nos permitirán trabajar mas a fondo con nuestro stock, podremos:
Planificar nuestros almacenes: podremos establecer cuándo realizar el aprovisionamiento de nuestros almacenes así como mantener el nivel de existencias para evitar o atender roturas de stock.
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
Gestión Avanzada Embalajes
TIPOS DE ARTICULO	        Ventas	Compra	Fábrica	Stock	Kit	Embalaje	 	 
Existencias Comerciales	      ☑	      ☑	 	         ☑	 	 	 	 
Materia Prima	 	                   ☑	 	      ☑	 	 	 	 
Semielaborado	 	 	                       ☑	  ☑	 	 	 	 
Producto Terminado	          ☑	 	          ☑	     ☑	 	 	 	 
Embalajes	 	                       ☑	  ☑	 	              ☑	 	 
Embalajes (Gestión Avanzada)	 	   ☑	  ☑	 	              ☑	 	 
Repuestos	                  ☑	      ☑	 	         ☑	 	 	 	 
Kit	                          ☑	      ☑	 	 	            ☑	 	 	 

Estructura y Niveles de Información
A tener en cuenta cómo es la estructura de datos del Tipo de Artículo y qué operativa tiene asociado cada nivel de la estructura: Tipos, Familias y Subfamilias.
Tipos / Familias/ Subfamilias
NIVEL DE INFORMACIÓN	Información heredada por los Artículos al asociar los Tipos, Familias y/o Subfamilias
Tipos	Codificación automática de artículos,Alcance Funcional,Imágen asociada al Tipo,Color asociado al Tipo,Tarifas de Venta
Familias	Codificación automática de artículos,Imágen asociada al Tipo,Color asociado al Tipo,Cuentas Contables (Regularización de Existencias),Descuentos Comerciales,Tarifas de Venta
Subfamilias	  Codificación automática de artículos,Cuentas Contables,Tarifas de Venta

Datos de Familias/Subfamilias de Artículo
Las Familias/Subfamilias representan un segundo nivel de clasificación y son dato obligatorio en el registro de cada una de las referencias de artículos.
Permite asociar a cada Familia las cuentas contables o descuentos comerciales que se necesite trasladar a los artículos. También permiten asociar las Características para configurar la gestión de tallas y colores del TPV o bien la generación automática de artículos que tengan en común una referencia global (tallas y colores).
A su vez, por cada familia se pueden establecer distintas subfamilias que otorgan un nivel adicional de análisis en el ámbito estadístico y también la codificación automática de sus artículos por tipo, familia y subfamilia.

Crear un Tipo de Artículo
Proceso:
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
Otros Datos:
Correlativo: número correlativo utilizado en la codificación automática simple de artículos.
☑ Característica 1, 2, 3,4 y 5: permite indicar qué características se van a gestionar en la gestión de tallas y colores.
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

Estados de Artículo
Muestra la información correspondiente a los distintos Estados susceptibles de asociar a cada uno de los artículos, productos o referencias.
Permite crear nuevos Estados que permitan identificar fases de la evolución de los artículos, como por ejemplo, los artículos obsoletos.
Proceso:
Acude a Estados de Artículos.
Datos:
Estado: código identificador del estado de artículo.
Descripción Estado: descripción detallada del Estado.
☑ Activo: implica entradas y salidas de stock.
☑ Visible TPV: se muestra en las de Venta TPV.
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
<table id="T_A_Identificacion">
    <caption class="caption">
Identificación del Artículo
  </caption>
    <tbody>
        <tr>
          <td width="10%" rowspan="6" class="Columna1_TbDatos">Codificación de Artículos</td>
          <td class="Columna2_TbDatos"><img src="../../../Recursos_S/Images/_Icons/pen.png" width="16px" height="16px"> (Contadores de Artículos)</td>
          <td class="Parrafo_TbDatos">Contadores asociados a la Entidad del Artículo. Por defecto se aplica el contador predeterminado de artículos. Si deseas cambiar de contador, selecciona aquí el que corresponda</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos"><img src="../../../Recursos_S/Images/_Icons/book_open.png" width="16px" height="16px"> (Codificación Avanzada)</td>
          <td class="Parrafo_TbDatos">Asigna el código obtenido del Criterio de Codificación Avanzada que corresponda según la información del artículo activo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Código</td>
          <td class="Parrafo_TbDatos">El código se puede obtener del <strong>Contador predeterminado</strong> de la entidad Artículos o bien de la <strong>Codificación Automática</strong> que proporciona el sistema.</td>
        </tr>
        <tr>
          <td rowspan="2" class="Columna2_TbDatos">Descripción</td>
          <td class="Parrafo_TbDatos">Texto que además de identificar al artículo, facilita su localización en procesos y consultas posteriores. Se puede actualizar/modificar durante lo procesos de gestión. Por ejemplo: para gestionar las compras de material de oficina se registra una única ficha de artículo cuya descripción es ‘material de oficina’. En la factura de compra se recoge el código de este artículo y en la descripción se modifica el literal ‘material de oficina’ por el del artículo ‘Agenda día página’.</td>
        </tr>
        <tr>
          <td class="Parrafo_TbDatos">En el <strong>apartado Idiomas</strong> puedes indicar la traducción de la descripción del artículo para que el sistema utilice las traducciones en función del idioma del Cliente/Proveedor. La traducción se traslada a las líneas de los documentos que acompañan cada fase del circuito comercial así como al dato de la Descripción Referencia Cliente/Proveedor presente en cada línea de los documentos comerciales (Pedidos, Albaranes y Facturas).</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Alias</td>
          <td class="Parrafo_TbDatos">-</td>
        </tr>
        <tr>
          <td width="10%" class="Columna1_TbDatos">Clasificación</td>
          <td class="Columna2_TbDatos">Tipo, Familia y Subfamilia</td>
          <td class="Parrafo_TbDatos">Conforma la clasificación del artículo para el Catálogo Comercial, por ejemplo. También traslada al artículo información de alcance funcional heredado del Tipo, la Familia o Subfamilia asociados.</td>
        </tr>
        <tr>
          <td width="10%" rowspan="2" class="Columna1_TbDatos">Vigencia</td>
          <td class="Columna2_TbDatos">Estado</td>
          <td class="Parrafo_TbDatos">Informa de la vigencia del artículo: activo, obsoleto, etc.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Disponible</td>
          <td class="Parrafo_TbDatos">Si la opción ☑ <strong>Disponible</strong> se encuentra desactivada no se permiten ni entradas ni salidas de stock. (Opción asociada al Estado y heredada del valor de <span class="Columna2_TbDatos">☑ Activo</span>de los Estados de Artículo).</td>
        </tr>
        <tr>
          <td rowspan="2" class="Columna1_TbDatos">Configurador de Producto</td>
          <td class="Columna2_TbDatos">☑ <strong>Configurable</strong></td>
          <td class="Parrafo_TbDatos">Indica que el artículo puede gestionarse mediante el <strong>Configurador de productos</strong>.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Familia Configurador</td>
          <td class="Parrafo_TbDatos">Identificador de la familia de configurador asociado al artículo activo. Este dato interviene en la gestión del configurador del producto.</td>
        </tr>
    </tbody>
</table>
<table id="T_A_General">
    <caption class="caption">
    General
    </caption>
    <tbody>
        <tr>
          <td width="10%" class="Columna1_TbDatos">Tipo de Artículo</td>
          <td class="Columna2_TbDatos">☑ Venta ☑ Compra ☑ Embalaje ☑ Genérico ☑ Gestión de Stock ... </td>
          <td class="Parrafo_TbDatos">Alcance funcional de la operativa a realizar con el artículo activo. Estas opciones se heredan del<strong> <a href="#A_TiposArticulos">Tipo de Artículo</a></strong> asociado. No se pueden modificar a nivel de Artículo. Las modificaciones han de realizarse en el Tipo de Artículo.</td>
        </tr>
        <tr>
          <td width="10%" rowspan="2" class="Columna1_TbDatos">Información adicional</td>
          <td class="Columna2_TbDatos">Observaciones</td>
          <td class="Parrafo_TbDatos">Texto libre con notas destacadas acerca del artículo activo. </td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Imágenes</td>
          <td class="Parrafo_TbDatos">Se muestra la imágen predeterminada, del Listado de imágenes asociado al artículo activo. Para acceder al Listado, utiliza el proceso <img src="https://portal.zucchettisp.es/Solmicro/Recursos/Images/_Icons/Boton_Proceso.svg" width="16px" height="16px"> <strong>Imágenes</strong>.</td>
        </tr>
    </tbody>
</table>
<table id="T_A_Financiero">
    <caption class="caption">
    Financiero
    </caption>
    <tbody>
        <tr>
          <td colspan="3" class="Columna1_TbDatos">&nbsp;</td>
        </tr>
        <tr>
          <td width="10%" rowspan="4" class="Columna1_TbDatos">Cuentas Contables <u>Compras</u></td>
          <td class="Columna2_TbDatos">Normal</td>
          <td class="Parrafo_TbDatos">Cuenta contable utilizada para compras nacionales/intracomunitarias.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Grupo</td>
          <td class="Parrafo_TbDatos">Cuenta contable utilizada para las compras a proveedores que hayamos identificado que pertenecen a un Grupo de empresas.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Importación</td>
          <td class="Parrafo_TbDatos">Cuenta contable utilizada para compras internacionales, es decir, aquellas realizadas a un proveedor "extracomunitario" (el país tiene activada la opción ☑ <strong>Extranjero</strong>).</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Importación Grupo</td>
          <td class="Parrafo_TbDatos">Cuentas contables utilizadas para las compras internacionales a proveedores del Grupo, es decir aquellas realizadas a un proveedor "extracomunitario" que pertenece a un Grupo (el país tiene activada la opción ☑ <strong>Extranjero</strong>).</td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">Cuentas Contables <u>Stocks</u></td>
          <td class="Columna2_TbDatos">Stock</td>
          <td class="Parrafo_TbDatos">Cuenta contable destinada a la <strong>Regularización de Existencias</strong> automática a partir del <strong>Cierre de Inventario</strong>.</td>
        </tr>
        <tr>
          <td rowspan="4" class="Columna1_TbDatos">Cuentas Contables <u>Ventas</u></td>
          <td class="Columna2_TbDatos">Normal</td>
          <td class="Parrafo_TbDatos">Cuenta contable utilizada para ventas nacionales/intracomunitarias.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Grupo</td>
          <td class="Parrafo_TbDatos">Cuenta contable utilizada para las ventas a clientes que hayamos identificado que pertenecen a un Grupo de empresas.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Exportación</td>
          <td class="Parrafo_TbDatos">Cuenta contable utilizada para ventas internacionales, es decir, aquellas realizadas a un cliente "extracomunitario" (el país tiene activada la opción ☑ <strong>Extranjero</strong>).</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Exportación Grupo</td>
          <td class="Parrafo_TbDatos">Cuentas contables utilizadas para las ventas internacionales a clientes del Grupo, es decir aquellas realizadas a un cliente "extracomunitario" que pertenece a un grupo (el país tiene activada la opción ☑ <strong>Extranjero</strong>).</td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">Cuentas Contables <u>Familia</u></td>
          <td colspan="2" class="Columna2_TbDatos">Muestra las cuentas contables asociadas a   la familia vinculada con el artículo, se utilizan en caso de no tener el   artículo información en las cuentas propias (Cuentas contables por artículo).</td>
        </tr>
        <tr>
          <td rowspan="4" class="Columna1_TbDatos">Impuesto: <u>IVA</u></td>
          <td colspan="2" class="Parrafo_TbDatos">Ver información detallada: <a href="IVA.AsignacionAutomatica">Gestión IVA. Asignación automática del impuesto IVA en la gestión de las Compras y Ventas.</a></td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Tipo IVA</td>
          <td class="Parrafo_TbDatos">Este valor no trabaja por sí solo, es decir, que no siempre será este IVA el que se asigne en los procesos de compra o venta, se requiere de una gestión y parametrización determinada para determinar cómo se va a realizar la Asignación IVA en las ventas o compras.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">% IVA Reducido</td>
          <td class="Parrafo_TbDatos">-</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">% IVA No Deducible</td>
          <td class="Parrafo_TbDatos"><p>En función de la actividad económica de la empresa, hay ciertas empresas que no pueden deducir el 100% del IVA soportado si no que sólo pueden deducir una cantidad de IVA de sus compras que sea proporcional al IVA que ha cobrado en sus ventas. En el campo % IVA No Deducible, registraremos el porcentaje de IVA que no se puede deducir del artículo. Partiendo de este porcentaje, al introducir las Facturas de Compra el Importe de IVA se separa automáticamente en: Deducible / No Deducible (los cuales se registrarán el la factura de dentro de los campos Imp. IVA No Deducible e Im. IVA Deducible), con su consiguiente efecto contable:        
            </p>
            <ul>
              <li>IVA deducible se lleva a una cuenta de IVA.            </li>
              <li>IVA no deducible supone mayor importe de compra (o gasto).          </li>
            </ul>
          <p>Finalmente, a final de año, hay que ajustar el porcentaje y realizar los correspondientes ajustes de cuotas, tanto desde el punto de vista fiscal (ficheros) como desde el punto de vista contable.</p></td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">Impuesto: IRPF</td>
          <td class="Columna2_TbDatos">☑ Retención IRPF</td>
          <td class="Parrafo_TbDatos">Se activa cuando el artículo que estemos registrando sea un concepto para retención de IRPF en una Factura. El porcentaje de IRPF a aplicar se indica en la ficha del Cliente y todos estos datos se utilizan en la factura de venta. <a href="../Impuestos/Impuestos.aspx#IRPF" target="_blank">Más información: Gestión IRPF.</a></td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">Impuestos Especiales</td>
          <td class="Columna2_TbDatos">Impuestos</td>
          <td class="Parrafo_TbDatos">Listados de Impuestos adicionales a utilizar en la gestión de Compras y  Ventas. Se aplican  <u>antes de IVA</u>. Por ejemplo: <a href="../Impuestos/Impuestos.aspx#D.PuntoVerde" target="_blank">impuesto Punto Verde.</a> </td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">Declaración Intrastat</td>
          <td class="Columna2_TbDatos">Partida Estadística</td>
          <td class="Parrafo_TbDatos">Partida arancelaria correspondiente al artículo. Este dato únicamente es de relevancia para la <a href="../Impuestos/Impuestos.aspx#D.Intrastat" target="_blank">Declaración Intrastat.</a></td>
        </tr>
    </tbody>
</table>
<table id="T_A_Clientes">
    <caption class="caption">
    Clientes
    </caption>
    <tbody>
        <tr>
          <td colspan="3" class="Parrafo_TbDatos">Muestra los <a href="../Clientes/Clientes.aspx" target="_blank">Clientes</a> a los que puede ir destinado este artículo, así como determinadas especificaciones para cada uno de ellos (Referencia del cliente para el artículo, precios especiales en función de la cantidad, etc).</td>
        </tr>
        <tr>
          <td width="10%" rowspan="4" class="Columna1_TbDatos">Cliente</td>
          <td class="Columna2_TbDatos">Código y Descripción</td>
          <td class="Parrafo_TbDatos">Código y Denominación del Cliente.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">☑ Principal</td>
          <td class="Parrafo_TbDatos">Indica quién es el cliente principal para las ventas del artículo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Referencia Cliente</td>
          <td class="Parrafo_TbDatos">Cómo denomina el Cliente al artículo activo. Permite identificar al artículo en el proceso de venta. Además si el cliente tiene un Idioma asociado, el sistema traslada la descripción del artículo tanto a las líneas de los procesos de venta (dato Descripción Referencia de Cliente) como a los documentos impresos que debamos enviarle. <a href:"a_idiomas"="">Más información: Gestión de Idiomas.</a></td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Revisión</td>
          <td class="Parrafo_TbDatos">Identifica el ‘número de revisión’ con la que trabaja el cliente. Información utilizada en la ‘oficina técnica’ para los pedidos realizados sobre las referencias que maneja. </td>
        </tr>
        <tr>
          <td rowspan="4" class="Columna1_TbDatos">Unidades/Precios</td>
          <td class="Columna2_TbDatos">Unidad de Venta</td>
          <td class="Parrafo_TbDatos">Unidad en la que se compra el artículo a este proveedor. Debe existir un <a href="#FactorConversion">Factor de Conversión</a> entre esta unidad y la unidad interna de almacenamiento del artículo si son distintas para que la operativa de la gestión de stocks sea correcta.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Unidad de Valoración</td>
          <td class="Parrafo_TbDatos">Unidad a la que se asocia el Precio de Venta.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Precio</td>
          <td class="Parrafo_TbDatos">Precio del Cliente para una unidad (de valoración y en la unidad de venta) artículo activo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descuentos 123</td>
          <td class="Parrafo_TbDatos">Descuentos línea que acompañan al precio anterior.</td>
        </tr>
        <tr>
          <td rowspan="3" class="Columna1_TbDatos">Precios por cantidades</td>
          <td class="Columna2_TbDatos">Cantidad desde</td>
          <td rowspan="3" class="Parrafo_TbDatos">Escalado de Cantidades, Precios y Descuentos 123 (línea).</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Precio</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descuentos 123</td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">EDI</td>
          <td class="Columna2_TbDatos">Código EDI</td>
          <td class="Parrafo_TbDatos">Código para el intercambio de datos electrónicos. Interviene en la <a href:"..="" ventas="" ventas.aspx#v_edi"="">Gestión EDI.</a></td>
        </tr>
        <tr>
          <td class="Columna1_TbDatos">Contrato</td>
          <td class="Columna2_TbDatos">Contrato/Oferta Comercial</td>
          <td class="Parrafo_TbDatos">Si las condiciones particulares se han recogido en una Oferta / Contrato comercial previa, bien desde ésta (al actualizar las condiciones) o bien manualmente, se indica el código de la oferta/contrato de origen.</td>
        </tr>
      <tr>
          <td class="Columna1_TbDatos">Bloqueo Cliente/Artículos</td>
        <td class="Columna2_TbDatos">☑ Bloqueado</td>
        <td class="Parrafo_TbDatos"><p>Indica que los procesos comerciales referentes al artículo activo han sido bloqueados para el cliente.</p>
          <ul>
            <li>No permite registrar nuevos:
              Ofertas Comerciales, Pedidos, Albaranes, Generar Pedidos desde Ofertas y
              Generar Albaranes desde Pedidos.              </li>
            <li>Sí permite registrar nuevos:
              
              Generar Facturas desde Albaranes o Nuevas Facturas.</li>
        </ul></td>
      </tr>
      <tr>
        <td rowspan="5" class="Columna1_TbDatos">Expediciones</td>
        <td class="Columna2_TbDatos"><img src="../../../Recursos_S/Images/_Icons/cube_yellow.png" width="16px" height="16px"> (Embalajes y Contenedores)</td>
        <td class="Parrafo_TbDatos">Acceso a los embalajes requeridos en la preparación de las expediciones al Cliente. Ver más información en <strong>Gestión de Embalajes</strong>.</td>
      </tr>
      <tr>
        <td class="Columna2_TbDatos">Tipo Contenedor</td>
        <td class="Parrafo_TbDatos">Muestra el Contenedor (contiene los embalajes).</td>
      </tr>
      <tr>
        <td class="Columna2_TbDatos">Piezas Contenedor</td>
        <td class="Parrafo_TbDatos">Cantidad de artículos.</td>
      </tr>
      <tr>
        <td class="Columna2_TbDatos">Tipo Embalaje</td>
        <td class="Parrafo_TbDatos">Muestra el Embalaje.</td>
      </tr>
      <tr>
        <td class="Columna2_TbDatos">Piezas Embalaje</td>
        <td class="Parrafo_TbDatos">Cantidad de artículos.</td>
      </tr>
      <tr>
        <td class="Columna1_TbDatos">Transportista</td>
        <td class="Columna2_TbDatos">Muelle</td>
        <td class="Parrafo_TbDatos">Muelle de carga.</td>
      </tr>
    </tbody>
</table>
<table id="T_A_Proveedores">
    <caption class="caption">
    Proveedores
  </caption>
    <tbody>
        <tr>
          <td colspan="3" class="Parrafo_TbDatos">Muestra los <a href="../Proveedores/Proveedores.aspx" target="_blank">Proveedores</a> a los que puede ir destinado este artículo, así como determinadas especificaciones para cada uno de ellos (Referencia del cliente para el artículo, precios especiales en función de la cantidad, etc).</td>
        </tr>
        <tr>
          <td width="10%" rowspan="3" class="Columna1_TbDatos">Proveedor</td>
          <td class="Columna2_TbDatos">Código y Descripción</td>
          <td class="Parrafo_TbDatos">Código y Denominación del Proveedor</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">☑ Principal</td>
          <td class="Parrafo_TbDatos">Indica quién es el proveedor principal para las compras del artículo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Referencia Proveedor</td>
          <td class="Parrafo_TbDatos">Cómo denomina el Proveedor al artículo activo. Permite identificar al artículo en el proceso de compra.</td>
        </tr>
        <tr>
          <td rowspan="4" class="Columna1_TbDatos">Unidades/Precios</td>
          <td class="Columna2_TbDatos">Unidad de Compra</td>
          <td class="Parrafo_TbDatos">Unidad en la que se compra el artículo a este proveedor. Debe existir un <a href="#FactorConversion">factor de conversión</a> entre esta unidad y la unidad interna de almacenamiento del artículo si son distintas para que la operativa de la gestión de stocks sea correcta.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Unidad de Valoración</td>
          <td class="Parrafo_TbDatos">Unidad a la que se asocia el Precio de Compra.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Precio</td>
          <td class="Parrafo_TbDatos">Precio del Proveedor para una unidad (de valoración y en la unidad de compra) artículo activo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descuentos 123</td>
          <td class="Parrafo_TbDatos">Descuentos línea que acompañan al precio anterior.</td>
        </tr>
        <tr>
          <td rowspan="3" class="Columna1_TbDatos">Precios por cantidades</td>
          <td class="Columna2_TbDatos">Cantidad desde</td>
          <td rowspan="3" class="Parrafo_TbDatos">Escalado de Cantidades, Precios y Descuentos 123 (línea).</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Precio</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descuentos 123</td>
        </tr>
    </tbody>
</table>
<table id="T_A_Idiomas">
    <caption class="caption">
    Idiomas
    </caption>
    <tbody>
        <tr>
          <td width="10%" rowspan="2" class="Columna1_TbDatos">Traducción (Descripción)</td>
          <td class="Columna2_TbDatos">Idioma</td>
          <td class="Parrafo_TbDatos">Código del idioma vinculado a la traducción de  la  descripción del artículo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descripción</td>
          <td class="Parrafo_TbDatos">Traducción de la descripción del artículo en el idioma seleccionado, este dato se muestra en los campos de   referencia de proveedor  o cliente en función del idioma de estos.</td>
        </tr>
    </tbody>
</table>
<table id="T_A_Analitica">
    <caption class="caption">
    Analítica
    </caption>
    <tbody>
        <tr>
          <td colspan="3" class="Parrafo_TbDatos">Muestra el desglose de la imputación analítica por centros de coste asociada al artículo. </td>
        </tr>
        <tr>
          <td width="10%" rowspan="3" class="Columna1_TbDatos">Centro de Coste</td>
          <td class="Columna2_TbDatos">Centro Coste</td>
          <td class="Parrafo_TbDatos">Centro de Coste</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descripción Centro Coste</td>
          <td class="Parrafo_TbDatos">Descripción Centro de Coste</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">%</td>
          <td class="Parrafo_TbDatos">Porcentaje asociado al centro de coste. Se le encargará que la suma de porcentajes de como resultado el 100%.</td>
        </tr>
    </tbody>
</table>
<table id="T_A_Alternativos">
    <caption class="caption">
    Artículos Alternativos
    </caption>
    <tbody>
        <tr>
          <td colspan="3" class="Parrafo_TbDatos">Artículos alternativos en caso de que el artículo no se encuentre disponible. Se considerará el artículo alternativo a nivel de movimientos de Stock (salida y entrada del artículo). La  gestión económica se realiza en función de las características del artículo no disponible o principal.</td>
        </tr>
        <tr>
          <td width="10%" rowspan="2" class="Columna1_TbDatos">Artículo Alternativo</td>
          <td class="Columna2_TbDatos">Código</td>
          <td class="Parrafo_TbDatos">Código del artículo alternativo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Descripción</td>
          <td class="Parrafo_TbDatos">Descripción del artículo alternativo. </td>
        </tr>
    </tbody>
</table>
<table id="T_A_Calidad">
    <caption class="caption">
    Calidad
    </caption>
    <tbody>
        <tr>
          <td colspan="3" class="Parrafo_TbDatos">Gestión de Calidad</td>
        </tr>
        <tr>
          <td width="10%" class="Columna1_TbDatos">Estado Homologación</td>
          <td class="Columna2_TbDatos">Homologación</td>
          <td class="Parrafo_TbDatos">Informa del estado en que se encuentra el proceso de homologación del artículo.</td>
        </tr>
        <tr>
          <td width="10%" rowspan="2" class="Columna1_TbDatos">Plan de Control</td>
          <td class="Columna2_TbDatos">Fecha Plan</td>
          <td class="Parrafo_TbDatos"> informa de la fecha de la última revisión del Plan de control del artículo.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Nivel Plan</td>
          <td class="Parrafo_TbDatos">Nivel de revisión del Plan de control del artículo, relacionado con el módulo de Calidad.</td>
        </tr>
        <tr>
          <td rowspan="3" class="Columna1_TbDatos">Control de Recepción</td>
          <td class="Columna2_TbDatos">Control de Recepción</td>
          <td class="Parrafo_TbDatos">Indica cuándo y cómo se ha de realizar el control de calidad en el proceso de recepción de mercancía. Las opciones son: Control Calidad, Siempre o Nunca.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">☑ Seguridad / ☑ Reglamentación</td>
          <td class="Parrafo_TbDatos">Opciones excluyentes de las que dependerá el que se muestre en los informes de calidad correspondientes (Pautas, etc.), unos símbolos u otros.</td>
        </tr>
        <tr>
          <td class="Columna2_TbDatos">Especificación</td>
          <td class="Parrafo_TbDatos">Especificaciones de calidad asociadas al artículo que pueden ser valores o bien descripciones con más detalle.</td>
        </tr>
    </tbody>
</table>

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
☑ Activo: Si esta marca está desactivada no se permiten ni entradas ni salidas de stock. Esta opción se haya vinculada al Estado asociado al artículo, por lo que el que esté activo  o no dependerá del estado asociado, por ejemplo una referencia cuyo estado es ‘obsoleto’ no se encontrará activo por lo que no podrá ser ni recibido, ni expedido. Le permite gestionar obsolescencias.
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
<table width="62%" height="250" border="0" align="center">
                <tbody><tr class="trHeaderManual">
                  <th width="30%">Referencia de Artículo</th>
                  <th width="12%">Unidad Almacén (Stock)*</th>
                  <th width="12%">Unidad Compra**</th>
                  <th width="12%">Unidad Fábrica**</th>
                  <th width="12%">Unidad Venta**</th>
                  <th width="12%">Factor Conversión</th>
                  <th width="10%">Estructura</th>
                </tr>
                <tr class="trChildManual">
                  <th class="trHeaderManual">Agua (Lt)</th>
                  <td>Litro</td>
                  <td><span class="Parrafo1_Cuerpo">Litro</span></td>
                  <td>Litro</td>
                  <td>Litro</td>
                  <td>1</td>
                  <td>Agua</td>
                </tr>
                <tr class="trChildManual">
                  <th class="trHeaderManual">Botella "Single" (1,5 Lts)</th>
                  <td>Litro</td>
                  <td>-</td>
                  <td>Botella 1.5</td>
                  <td>Botella 1.5</td>
                  <td>1,5</td>
                  <td>Agua + Botella + Tapón</td>
                </tr>
                <tr class="trChildManual">
                  <th class="trHeaderManual">Bidón "Hogar" (5 Lts)</th>
                  <td>Litro</td>
                  <td>-</td>
                  <td>Bidón 5</td>
                  <td>Bidón 5</td>
                  <td>5</td>
                  <td>Agua + Bidón 1 + Tapón</td>
                </tr>
                <tr class="trChildManual">
                  <th class="trHeaderManual">Bidón "Oficina" ( 10 Lts)</th>
                  <td>Litro</td>
                  <td>-</td>
                  <td>Bidón 10</td>
                  <td>Bidón 10</td>
                  <td>10</td>
                  <td>Agua + Bidón 2  + Tapón</td>
                </tr>
</tbody></table>
Establecidad esta matriz de conversiones en la información del Artículo (apartado Unidades/Precio) la operativa será la siguiente:
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
3. Configurar la codificación automática
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
Efectos:
Código y Descripción: El código propuesto se crea a partir del código del artículo padre añadiéndole el código de las variables que han participado. Siguiendo con el ejemplo planteado, se proponen los códigos: PLCD003_14, PLCD003_18, PLCD003_20 y PLCD003_22.
La descripción propuesta se crea a partir de la descripción del artículo padre añadiéndole el texto descriptivo de las variables utilizadas, según el ejemplo se propone: Pantalla PC LCD modelo ZK10_14’’, etc.
En el apartado Características (apartado: Características Artículos) puedes visualizar las características y valores del artículo activo así como del artículo ’padre’ a partir del que se ha generado. Posteriormente puedes utilizar estos valores en la búsqueda de artículos, de gran utilidad en determinados ámbitos como puede ser el TPV donde se necesita acceder rápidamente a la consulta de referencias en función de sus propiedades.

Parametrizar la Producción
Permite identificar cómo realizamos el descuento de materiales y las entradas de producto terminado resultante del proceso de fabricación.
Proceso:
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
Proceso:
Acude a Artículos
Localiza el artículo y ejecuta el proceso  Ir a Ficha Coste.

Estructura Multinivel (Rutas y Estructuras)
Los datos de las Rutas y Estructuras del artículo están agrupados en distintos apartados lo que permite un acceso multinivel a la información así como realizar acciones de forma agrupada. Solmicro ERP incorpora una pantalla en la que se puede consultar y manejar esta información de forma gráfica e intuitiva.
Proceso:
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
Se utiliza en artículos con estructura, de tipo ☑ Fábrica o ☑ Kit.
Proceso:
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
Proceso:
Acude a Actualizar Ventas con Ultimo Precio Estándar, localizamos y seleccionamos los artículos que vamos a actualizar.
Indica la Fecha a partir de la cual cambiaremos el precio de coste de las ventas.
Ejecuta el proceso Actualizar Precio Estándar.
El precio de coste de las ventas se ha modificado, así como todos los movimientos del histórico de movimientos, posterior a esa fecha.

Actualizar los Plazos de Compra / Fábrica
Este proceso atañe tanto al circuito de compras como al de fabricación; permite modificar el plazo necesario para comprar o fabricar un artículo.
Proceso:
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
Proceso:
Acude a Almacenes, inicia un nuevo registro. La información obligatoria es: Código y Descripción.
Selecciona la opción ☑ Activo para permitir las recepciones y las expediciones de mercancía.
Selecciona la opción ☑ Empresa para considerar este almacén en el proceso de Valoración de Almacenes.
Indica el Centro de Gestión asociado al almacén y selecciona la opción ☑ Principal para destacarlo sobre otros almacenes del mismo centro de gestión.
 Ubicaciones del almacén. Este proceso afecta a la gestión de lotes – ubicación. En el siguiente proceso veremos cómo se realiza el registro de una ubicación.
Ubicaciones de almacén
Proceso:
Acude a Almacenes y localiza el Almacén en el que se van a identificar las Ubicaciones.
Accede a las Ubicaciones a través del botón .
Puedes inventariar el listado de ubicaciones asociado al almacén seleccionado: Pasillo A, Pasillo Central, Pasillo A - Balda1, etc.
Indica una ubicación como ☑ Predeterminada que será la que propone el sistema proponga en determinados procesos como, por ejemplo, en la recepción de un Lote de artículos.
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
☑ Depósito.
☑ Empresa: indica que las existencias son nuestras y por ello deben tratarse en la Valoración de almacenes y/o en los Cierres contables de almacén (Inventario).
Almacén de Depósito asociado al Cliente
Para asociar el almacén al cliente e identificar el destino de la mercancía inicial utilizamos las direcciones de envío al cliente seleccionando una de ellas como la correspondiente al Almacén de Depósito.
Proceso:
Acude a Clientes, apartado Direcciones.
Crea o localiza la dirección que identifica la ubicación del almacén e indica su código en el dato Almacén de Consigna.
Almacenes Envases Retornables
Utilizados en la Gestión de Envases Retornables en la que "necesitamos" un almacén, ficticio o real ("casa del cliente") para por un lado, valorar los envases de nuestra propiedad y por otro, utilizar el dato del almacén como origen en la devolución de los envases retornables.
Información del Almacén de Envases en el registro de almacenes:
☑ Empresa: indica que las existencias son nuestras y por ello deben tratarse en la Valoración de almacenes y/o en los Cierres contables de almacén (Inventario).
Almacén de Envases
Para asociar el almacén al cliente e identificar el destino de la mercancía inicial utilizamos las direcciones de envío al cliente seleccionando una de ellas como la correspondiente al Almacén de Depósito.
Proceso:
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
Proceso:
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
☑ Activo: opción que si está desactivada impide las entradas o salidas de stock.
Cuenta Contable Stock: necesaria para la Regularización de Existencias e Inventario Permanente. (Apartado Cuentas Contables)
Almacenes
Almacenes: listado de Almacenes en los que puede ubicarse el Artículo. Existirá un almacén predeterminado.
☑ Stock Negativo: permite realizar movimientos con stock negativo.
☑ Lotes-Ubicación: 1 Lote: N Artículos. Ejemplo: los artículos resultantes de cada orden de fabricación llevan asociados un número de lote donde se indica la OF que los ha originado junto a la fecha y hora de fabricación, este número identificador es común para todos los productos obtenidos en la OF.
☑ Nº de Serie: 1 Nº Serie = 1 Artículo. Ejemplo: empresa de Alquiler de Vehículos. Su artículo central es el vehículo, donde cada registro del mantenimiento de artículos identifica a un modelo de ellos pero resultará imprescindible identificar de forma inequívoca cada una de las unidades de un mismo artículo, es decir, tenemos en el parque 5 automóviles del tipo “x” (modelo, marca, cc, etc) para identificarlos tenemos una ficha de artículo donde se dice que hay 5 unidades, utilizaremos los números de serie para identificarlos de forma individual y cada número de serie se identificará con el número de matrícula de cada unidad. Cada vez que realicemos un movimiento de stock, el sistema solicitará el correspondiente número de serie.
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
Existe un control que puede afectar al stock, éste es el Estado de Homologación asociado al artículo que debe permitir que se pueda expedir. Se informa del estado en el campo ‘Estado de homologación’ mostrado en la solapa Calidad, de la ficha del artículo activo. En los Estados de Homologación se asocia a cada uno de los estados la característica de ☑ Expedible. De este modo la homologación de un artículo incidirá en su posible expedición o no.

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
☑ Activo: en caso de estar desactivado, no se permiten ni entradas ni salidas de mercancía.
☑ Bloqueado: si el valor asociado es positivo, sólo se permitirán realizar transferencias y movimientos de entrada a este almacén, no se permiten realizar salidas de mercancía.
Lote:
☑ Bloqueado: el sistema controlará que no se puedan realizar expediciones para este lote. Puede gestionar esta marca en la pantalla Consulta de Lotes.
A continuación detallaremos los procesos referentes a la actualización y los movimientos de Stock:

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
Proceso:
Acude a Parámetros.
Localiza el parámetro: HIST_MOV | Movimientos de Stock: Contador.
En el dato Valor, Indica el código del Contador previamente generado.
Movimientos Automáticos
Los movimientos automáticos son desencadenados por la actualización del stock.
Cada vez que se realice una actualización (ya sea automática o manual desde las pantallas de Actualización de Compra / Venta), el sistema generará un movimiento que quedará registrado en el Histórico de movimientos.
En los casos en los que se realicen modificaciones sobre los albaranes o facturas, el sistema realizará un movimiento de corrección que compensen los movimientos involucrados.
Movimientos Manuales
En este mantenimiento están registradas las fichas de todos los movimientos realizados, incluyendo los que se generan automáticamente.
Utilizando este programa podrá registrar un movimiento manual:
Acude a Movimientos Manuales y genera un nuevo registro  (F8).
Indica los datos del movimiento:
Fecha en la que se realiza (por defecto se propone la actual).
Selecciona el tipo de movimiento del listado de los tipos de movimientos "manuales"(☑ Manual).
Almacén en que se va a generar el movimiento.
Indique los datos del artículo (líneas).
Una vez registrado el movimiento no es posible modificarlo o eliminarlo. Sin embargo, puedes realizar las correcciones pertinentes.
Corrección de Movimientos
Los movimientos de corrección se generan automáticamente cuando se realiza algún cambio en la información que repercute en un movimiento de stock ya realizado, por ejemplo: en in inventario, indicamos una cantidad, y posteriormente en la misma fecha de ese inventario indicamos otra.
Los movimientos de corrección se registran en el mismo Movimiento o bien puedes consultarlo en el Histórico de movimientos.
Movimientos manuales de stock: se muestra una línea de tipo “CR” en color rojo. Para ver estos datos, debemos asegurarnos que la opción ☑ Mostrar movimientos de corrección esté activada.
Histórico de Movimientos: filtrando por tipo de movimiento = Corrección. Para ver estos datos, debemos asegurarnos que la marca ☑ Mostrar correcciones esté activada.
Movimientos de Ajuste de Stock
Permite realizar ajustes puntuales del stock.
Proceso:
Acude a Ajustes.
Localiza el almacén y / o artículos que desea ajustar.
Sitúate en la línea del artículo > stock, e indique el stock total existente.
Pulsa directamente sobre el botón  para ejecutar el procedimiento.
Efectos:
El sistema generará un movimiento de tipo ajuste + (positivo) o tipo ajuste – (negativo) para actualizar el stock. Puedes comprobarlo en el  Histórico de Movimientos.
Histórico de Movimientos
El sistema mantiene un registro permanente de todas las transacciones de almacén. Para visualizar el conjunto de los movimientos de stock realizados, acuda a la consulta de movimientos.
Cada vez genera un movimiento de stock, sea por la causa que fuere (expediciones, consumo, traslado, inventario, etc.), este movimiento quedará registrado en el sistema y podremos consultarlo utilizando esta pantalla con todos los datos que estén relacionados:
La fecha del movimiento.
El tipo del movimiento: una transferencia, entrada o salida de producto (Cod.).
El artículo y la cantidad que se ha movido.
El lugar del que se ha movido (Almacén).
El número de artículos que quedan en el almacén después del movimiento (Acumulado).
Los movimientos que han sufrido algún tipo de modificación, activando la marca ☑ Mostrar Correcciones de la zona de los criterios de selección.
Ejemplo: en se ha generado un movimiento de stock a partir de un albarán, posteriormente se requiere modificar la cantidad de éste. Al actualizar nuevamente el stock, el sistema deshace el primer movimiento, y genera el nuevo movimiento donde recoge la cantidad definitiva. El movimiento que se ha deshecho pasará a ser un movimiento de corrección (Tipo de Movimiento = Corrección), y se representa en color rojo.
Los precios reales de cada movimiento (precio estándar, última compra, medio y FIFO) *Ver Nota.
Nota: la anexión de los precios reales en cada movimiento (estándar, última compra, precio medio y FIFO) tiene como objetivo agilizar el proceso de valoración de stocks ya que el sistema no tendrá que calcularlos cada vez que requiera valorar el almacén.Estos cambios tienen repercuten en el proceso de la valoración del stock (que incide en los apartados de valoración de stock y cierres de inventario).

Bloquear un almacén
Para casos en los que se requiera no utilizar un almacén ni la mercancía que este tenga en existencia. Este proceso nos permite bloquear un almacén impidiendo la expedición de su mercancía. Permite bloquear el almacén de forma que no se pueda realizar ningún movimiento de stock contra él.
Proceso:
Acude a Almacenes y localiza el almacén a bloquear.
Selecciona la opción ☑ Bloqueado.

Valorar el Almacén
Un aspecto fundamental es conocer ‘cuánto vale mi almacén’ para ello debemos saber dónde, cuánto y a qué precio está almacenado el inventario. Recuerde que las existencias de almacén se valoran en la unidad interna de cada artículo.
I) Aspectos de la aplicación a tener en cuenta antes de realizar la valoración del almacén
En este apartado detallamos una serie de conceptos que debe tener claros antes de realizar la valoración de sus almacenes:
Cálculo de los criterios de valoración: PMP, FIFO, Ultima Compra, Estándar
El valor de nuestras existencias puede variar dependiendo de muchos factores, por ello al momento de calcular el valor de nuestros almacenes deberemos tener en cuenta distintos criterios aplicables a dicho cálculo, de forma que podamos saber siempre, su valor más exacto.
Los criterios de Valoración son la base para el cálculo del valor de nuestro almacén y son:
Precio Medio
El precio medio nos permite obtener el valor medio de las existencias que había al inicio y de las entradas ponderadas según sus cantidades. Este se calcula siempre que se produce un movimiento de entrada y se graba en el histórico de movimientos.
Para cada artículo, podremos consultar este dato desde la solapa Almacenes > último movimiento.
Ejemplo de Cálculo del Precio Médio
Supongamos que nuestra empresa comercializa un producto y se han registrado los siguientes movimientos:
1 Enero | Inventario inicial: 500 ud., precio unitario 100 €.
15 febrero | compra 100 ud., precio unitario 105 €.
7 marzo | venta 300 ud., precio unitario 127 €.
22 abril | compra de 250 kg. Precio unitario = 110 €.
19 mayo | venta de 300 kg. Precio unitario = 135 €.
Los movimientos se registran en el sistema de la siguiente forma, ofreciendo el cálculo del precio medio como indicamos:
<table width="80%" align="center">
    <tbody><tr class="trHeaderManual">
              <th width="100" height="31">Fecha</th>
              <th width="100">Tipo Movimiento</th>
              <th width="100">Cantidad</th>
              <th width="100">Precio Unitario</th>
              <th width="100">Existencias</th>
              <th width="291">Precio Medio </th>
              <th width="238">Valoración del Almacén</th>
            </tr>
            <tr class="trChildManual">
              <td height="30">01 / enero</td>
              <td>IN (inventario)</td>
              <td>500</td>
              <td>100 €</td>
              <td>500</td>
              <td>100€</td>
              <td>50,000 €</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">15 / febrero</td>
              <td>E5 (Input)</td>
              <td>100</td>
              <td>105 €</td>
              <td>600</td>
              <td><p><img src="../../../Recursos_S/Images/Stocks/Stocks_clip_image002.png"></p></td>
              <td>60,498 €</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">07 / marzo</td>
              <td>S1 (Output)</td>
              <td>-300</td>
              <td>127 €</td>
              <td>300</td>
              <td>100.83€</td>
              <td>30,249 €</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">22 / abril</td>
              <td>E5 (Input)</td>
              <td>250</td>
              <td>110 €</td>
              <td>550</td>
              <td><p><img src="../../../Recursos_S/Images/Stocks/Stocks_clip_image003.png"></p></td>
              <td>57,750 €</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">19 / mayo</td>
              <td>S1 (Output)</td>
              <td>-300</td>
              <td>135 €</td>
              <td>250</td>
              <td>105€</td>
              <td>26,250 €</td>
            </tr>
  </tbody>
</table>
Precio FIFO
La valoración del almacén mediante el métido FIFO (Fist in First Out), presume que el primer producto ingresado en el almacén, será el primero en salir por efectos de inventario. El precio se calcula siempre que se produce un movimiento de entrada/salida, y lo graba en el histórico de movimientos.
<table width="80%" align="center">
            <tbody><tr class="trHeaderManual">
              <th width="100" height="31">Fecha</th>
              <th width="100">Tipo Movimiento</th>
              <th width="100">Cantidad</th>
              <th width="100">Precio Unitario</th>
              <th width="100">Existencias</th>
              <th width="291">Precio FIFO</th>
              <th width="238">Valoración del Almacén</th>
            </tr>
            <tr class="trChildManual">
              <td height="30">01 / enero</td>
              <td>IN (inventario)</td>
              <td>500</td>
              <td>100 €</td>
              <td>500</td>
              <td>100€</td>
              <td>&nbsp;</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">15 / febrero</td>
              <td>E5 (Input)</td>
              <td>100</td>
              <td>105 €</td>
              <td>600</td>
              <td><p>&nbsp;</p></td>
              <td>&nbsp;</td>
            </tr>
            <tr class="trChildManual">
              <td height="25">07 / marzo</td>
              <td>S1 (Output)</td>
              <td>-300</td>
              <td>127 €</td>
              <td>300</td>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">22 / abril</td>
              <td>E5 (Input)</td>
              <td>250</td>
              <td>110 €</td>
              <td>550</td>
              <td><p>&nbsp;</p></td>
              <td>&nbsp;</td>
            </tr>
            <tr class="trChildManual">
              <td height="30">19 / mayo</td>
              <td>S1 (Output)</td>
              <td>-300</td>
              <td>135 €</td>
              <td>250</td>
              <td>&nbsp;</td>
              <td>&nbsp;</td>
            </tr>
          </tbody></table>
Precio Última Compra
Representa el precio con el que se ha comprado un artículo por última vez. Dentro de nuestra aplicación, este dato se obtiene del último albarán de compra del artículo, actualizado, y se vuelca automáticamente en la solapa “precios” de la ficha del artículo, apartado última compra.
Precio Estándar
Se trata del precio que establecemos para el coste de adquisición del artículo. El precio estándar se considera principalmente en los procesos de Compra y de Producción ya que en las ventas utilizamos la gestión de tarifas para el establecimiento de los precios de venta.
Debemos tener en cuenta que en caso de un semielaborado (es decir que un artículo que formará parte de una estructura de producción) el precio estándar de dicho artículo corresponde al precio antes de la fabricación ya que durante ésta se añadiran a dicho precio, los costes de materiales, mano de obra, etc.
Nota: para calcular en el precio estándar de un artículo teniendo en cuenta los costes de la producción, utilizaremos el módulo de Costes.

Actualización Precio Artículo
Como ya hemos visto, el Precio Medio es calculado por el sistema en base a las entradas ponderadas según sus cantidades. Sin embargo por las prácticas de las empresas, el artículo en almacén puede variar de precio, dejando obsoleto el precio calculado y teniendo que hacer una inserción manual.
Con esta herramienta podremos fijar un precio medio a una fecha, manualmente para un artículo, de forma que no pueda recalcularse en caso de cambios en movimientos anteriores y sea un punto de partida para realizar el calculo en movimientos posteriores.
Para realizar este proceso:
Acudimos a la pantalla de actualización de precios de artículos e indicamos la fecha a la que queremos realizar la consulta.
Por defecto los criterios: Activo = Si, y Criterio de Valoración = Precio Medio, ya vienen dados, ya que la pantalla solamente nos va a permitir fijar precios medios.
Ejecutamos la consulta y veremos en pantalla:
Fecha: muestra la fecha en la que se ha valorado cada línea.  
Stock a Valorar: el stock que había en la fecha indicada. Las líneas mostradas en color rosa, indican que el stock a valorar es cero, con lo que el precio medio en este momento se va a resetear, por lo que imputar un nuevo precio en esta línea no va a tener ningún efecto.
Precio: precio según criterio de valoración. Como los filtros Criterio de Valoración = Precio Medio, todos los precios mostrados en este campo corresponden al Precio Medio. Las columnas correspondientes a los criterios de valoración (PM, FIFO, Estándar…)
Filtramos por el artículo cuyo precio queremos modificar.
Localizamos la fecha en la que queremos fijar el nuevo precio y en el campo “Nuevo Precio” indicamos el valor deseado.
Si volvemos a la consulta de movimientos, veremos que se graba un movimiento de tipo APM, a fecha indicada con cantidad 0 (ya que solo queremos manipular el precio) fijando así el precio.
En caso de que se realicen cambios en movimientos anteriores a la fecha en la que hemos fijado, el precio siempre se mantendrá con el mismo valor que hayamos fijado.
En fechas posteriores al valor fijado, ya se comporta normalmente (aplicando la fórmula de PMP).

Cálculo del precio en las entradas a almacén
Algunos criterios de la valoración de almacenes se basan en los precios de los movimientos de entrada. Las entradas se clasifican de la siguiente manera:
Albaranes de compra: las entradas originadas por albaranes de compra tendrán el precio del albarán de compra.
Ordenes de fabricación: las entradas de productos terminados o semielaborados de fabricación tendrán el precio estándar. Nota: el criterio de valoración del producto terminado o semielaborado, debe ser precio estándar (Artículo > Almacenes > Criterio de Valoración = Precio Estándar).
Movimientos de Transferencias: al realizar una transferencia entre almacenes el precio de la entrada al almacén destino es igual al precio de salida almacén origen. Nota: existen casos en los que esta norma no aplica ya que puede ser manipulada por el usuario en casos de ajustes o inventarios, en este caso ver el apartado de recalculo de precio en las transferencias de entrada.
Movimientos de Inventario y Ajuste: el precio de entrada se corresponde al del criterio de valoración del artículo. Es posible modificar manualmente estos precios de forma que en lugar de ser el criterio de valoración del artículo, sea el que nosotros indiquemos.
Movimientos de entrada manuales: en el momento de crear un movimiento de entrada manual, indicaremos el precio manualmente. En todos los casos si el precio es cero se ofrecerán dos opciones según lo que tenga indicado en el parámetro STPREC_MOV | Entrada de Stock: permitir precio = 0: 1: Realizar las entradas valoradas a precio cero. 0: Coger el precio del criterio de valoración del artículo (ficha artículo > solapa almacenes > Criterio de Valoración).

Recalcular el precio de entrada en las transferencias
En las transferencias entre almacenes, el precio de la entrada se corresponde con el precio al que sale del almacén origen.
Sin embargo existen casos en que por algún motivo esto no es así.
Por ejemplo:
El movimiento E5 (albarán de compra) tiene una entrada con un precio de 20€ (que es el que está en el documento).
Los siguientes dos movimiento corresponden a un ajuste, donde:
La salida del almacen 01 (T-) sale efectivamente con un valor de 20€ (para este caso no tenemos en cuenta el Precio A, ya que es irrelevante en las salidas, nos fijamos en el precio medio, que es el criterio de valoración para este artículo en concreto).
La entrada al almacén 02 (T+) es de 15€.
Vemos que en este ejemplo, el precio de salida de un almacén no corresponde al de entrada, como debería ser lo habitual... Este caso puede darse en muchas ocasiones ya que puede pasar que durante la transferencia (donde podemos indicar el precio de entrada al almacén) el artículo se haya desvalorizado y por ello mermado el precio, por ello el sistema no recalcula el precio de entrada de la transferencia (T+).
Pero si no es este caso ¿qué sucede si no que se trata de un error y el precio debería ser recalculado?
Supongamos que el ejemplo anterior se ha originado porque el usuario indica el precio de entrada original del albarán de compra (E5) a 15€, se produce la transferencia de almacén y después el usuario se da cuenta de que el precio indicado en el albarán de compra era erroneo y cambia el precio del albarán a 20€.
Para este caso tendremos que acudir a Consulta para recálculo de precio en las transferencias de entrada (Recalcular Transferencia Entrada):
En esta pantalla veremos todos los artículos cuya salida de origen en una transferencia no tiene el mismo precio que en la entrada a destino de la misma transferencia. Es decir, aquellas que no cumplen la norma "en las transferencias entre almacenes, el precio de la entrada se corresponde con el precio al que sale del almacén origen".
Una vez en esta pantalla:
Localizamos el movimiento que no cumple con la norma por un error.
Lo seleccionamos y ejecutamos el proceso Recalcular Transferencia.
El movimiento desaparece de la pantalla ya que el precio de entrada ha sido recalculado
Acudimos a la consulta de movimientos, donde podremos ver que el movimiento de ajuste de entrada ya corresponde con el de salida. Es decir, en este ejemplo serían 20 €.

Cálculo del precio en las salidas de almacén
Se considera como Salida de artículos:
En el proceso comercial: los movimientos generados por Albaranes de Venta.
En el proceso de producción: el consumo de materiales.
Etc...
En cualquir caso, el precio de la salida depende de lo que se indique en el campo "Recalcular Valoración en Movimiento de Salida", definido a nivel de artículo (solapa almacenes):
Mantener precio de salida: se trasladará al movimiento el mismo precio que se haya indicado en el documento (albaran de venta, movimiento manual...).
Recalcular: el precio del movimiento será el precio según el criterio de valoración del artículo.

Valoración del Inventario (Cantidades e Importes)
Podrá obtenerse a cualquiera de los precios alternativos siguientes: Estándar, Precio medio ponderado, y precio FIFO.
Además de la valoración de los almacenes actuales puede procederse a la valoración de los almacenes “a fecha atrás”. Habitualmente es el sistema de valoración empleado para poder obtener el inventario correspondiente en el cierre de cada mes sin necesidad de bloquear, durante los primeros días del mes siguiente, los procesos de almacén.

Calcular el valor del stock de una fecha determinada
Este procedimiento se realiza en la pantalla Valoración de Almacenes.
Esta pantalla podrá consultar el valor del stock en una fecha establecida y para todos los criterios de valoración.
Antes de iniciar el proceso tenga en cuenta que el cálculo de valoración (PMP, estándar y FIFO) se realiza por cada movimiento de stock y que esta pantalla obtiene su valores de los datos almacenados en el histórico de movimientos. Esto quiere decir que para que pueda ejecutar este nuevo proceso debe de haber información previa de movimientos realizados con esta nueva gestión.
Proceso:
Acude a Valoración de Almacenes e indica la Fecha Cálculo.
Ejecuta la consulta.
Efectos:
Los datos se obtienen directamente del histórico de movimientos a fecha del cálculo. Si no existe un movimiento en esa fecha recoge los del inmediatamente anterior.
Datos del Artículo: Tipo, familia, el criterio de valoración asignado al artículo...
Fecha: El sistema revisa si hay un movimiento en la fecha de cálculo y si no hay, ofrece la fecha del movimiento inmediatamente anterior.
Stock físico del artículo en el movimiento a fecha de cálculo.
Precio: muestra el precio del artículo a fecha de cálculo y según su criterio de valoración, es decir que este campo siempre tener el mismo valor que el campo que corresponda a su criterio de valoración: precio std, ultima compra, fifo...
Importe: muestra el importe al que ascienden los artículos en la fecha de cálculo y según su criterio de valoración, es decir que este campo siempre tener el mismo valor que el campo que corresponda a su criterio de valoración: importe precio std, importe ultima compra, importe fifo...
Precio Medio: recoge el precio medio del artículo en la fecha de cálculo.
Importe Precio Medio: calcula el importe según el precio medio y el stock a fecha.
Precio Std: recoge el precio estándar del artículo a fecha de cálculo.
Importe Precio Std: calcula el importe segín el precio std y el stock a fecha.
Precio Ultima Compra: recoge el precioúltima compra a fecha de cálculo.
Importe Precio Ultima Compra: calcula el importe según el precio ultima compra y el stock a fecha.
Precio FIFO Fecha: recoge el precio FIFO calculado segun la fecha del movimiento, del artículo a fecha de cálculo.
Importe Precio FIFO Fecha: calcula el importe según el precio FIFO fecha y el stock a fecha.
Precio FIFO Fecha Documento: recoge el precio FIFO calculado segun la fecha del documento, del artículo a fecha de cálculo.
Importe Precio FIFO Fecha Documento: calcula el importe según el precio FIFO documento y el stock a fecha.

Inventarios de Existencias
La gestión del stock se inicia con el Inventario de  los artículos, por lo que es recomendable realizar un Inventario Inicial y que este sea el primer movimiento de stock que exista en su registro.
Los efectos del proceso de Inventario son:
Quedará informado en la ficha del artículo, cuándo se ha realizado el último inventario por almacén (solapa Almacenes).
Evidencia del inventario, representada por el correspondiente movimiento de stock en el que se podrá consultar la fecha del inventario, así como los artículos inventariados y resto de información: cantidad inventariada, stock físico final y precio al que se valora el movimiento (según el criterio de valoración asociado al artículo).
En este apartado se detalla la información para realizar un inventario en el momento que lo requiera.
Configuración Inicial
Estos datos los tendrá en cuenta la primera vez que trabaje con inventarios o si, en cualquier otro momento, es necesario cambiar su parametrización.
Movimiento de Inventario
El Inventario se considera un movimiento de almacén. El movimiento de inventario se considera una “inicialización de stock” ya que establece una nueva cantidad de artículos en almacén.
El movimiento de inventario quedará registrado en el histórico de movimientos. Debemos configurar el sistema para indicar si este movimiento se debe registrar como primer o último movimiento del día.
Primer movimiento del día: el stock indicado en el inventario será el primer movimiento del día, con lo que el stock físico final reflejará el stock de inventario y posteriormente le aplicará los ajustes resultado de otros movimientos de entrada y salida de stock.
Último movimiento del día: el stock indicado en el ajuste será el stock físico final que se mostrará en la ficha de los artículos implicados, no teniendo en cuenta las entradas y salidas de ese día a efectos de stock físico final.
Proceso:
Acude a Parámetros.
Localiza el parámetro: Situación del movimiento de inventario: Primer movimiento – Último movimiento (STTIPOINV).
Selecciona uno de los valores siguientes:
0 | Primer Movimiento: el inventario será el primer movimiento del día.
1 | Último Movimiento: el inventario será el último movimiento del día.

Hacer un Inventario
Proceso:
Acude a Inventario, indica la Fecha de Inventario.
Utiliza los criterios de consulta y ejecute la consulta para obtener en pantalla los artículos objeto del inventario.
Selecciona las líneas a procesar.
Indica la cantidad inventariada en el dato: Stock.
En caso de que el artículo estuviera gestionado por Números de Serie o Lotes, se mostrarán los siguientes iconos:  Gestión de Lotes /  Gestión de Números de Serie.
Para registrar el stock, pulsa sobre estos iconos e indica los datos del Lote (y la fecha de caducidad, si procede) o Número de Serie a inventariar.
Selecciona el proceso Actualizar Stock.
Efectos:
Se muestra el Detalle de Actualización de Stock donde se indica si se ha realizado correctamente el proceso.
En la información de los Artículos inventariados, apartado Almacenes se muestra en la línea del almacén inventariado:
Aparece como ☑ Inventariado y se informa de la Fecha Último Inventario.
Aparece actualizado el dato del Stock Físico con la cantidad indicada en el proceso de Inventario.
En la Consulta de Movimientos (histórico de movimientos) veremos que se ha generado el movimiento de stock de tipo “Inventario” con los datos indicados en el Inventario.
Ejemplos:
Ejemplo 1
Día actual: 02/04/10 Stock Físico: 350
02/04: Hacemos un inventario para el día 20/03/05 mediante el que indicamos la cantidad de 200.
El día 23/03 ha habido un movimiento de salida de 125 unidades.
Resultado: se mostrará como dato para el stock físico de hoy, tras realizar el inventario: 75 unidades (200 - 125)
Ejemplo 2
Día actual: 02/04/10 Stock Físico: 350
02/04: Hacemos un inventario para el día 02/04/10 mediante el que indicamos la cantidad de 200.
Resultado: se mostrará como dato para el stock físico de hoy, tras realizar el inventario: 200 unidades.

Inventariar usando Excel
Este proceso nos permite integrar las cantidades de nuestro inventario desde un fichero excel. Se utiliza en casos en que la persona encargada de realizar el inventario no tenga acceso a la aplicación.
Realizamos el proceso en dos pasos:
Listamos los artículos a inventariar y exportamos el listado a un fichero excel y se lo entregamos al responsable de almacén.
Se completa las cantidades de inventario en el fichero excel.
Importamos el listado con las cantidades de Inventario completadas.
Preparar el listado de Inventario (exportar datos)
Proceso:
Acude a Inventarios, localiza los artículos / almacenes a inventariar.
Con el listado en pantalla, ejecuta el proceso  Generar Fichero Excel.
Efectos:
Obtenemos un fichero excel con el listado de artículos (mostrados en pantalla) y los siguientes datos:
Campos completados: Artículo, Descripción, Almacén, Stock Físico
Campos para ser completados durante el Inventario: Lote, Ubicación, Stock Lote-Ubicación UD1, Stock Lote-Ubicación UD2, Fecha Caducidad, Nuevo Stock UD1, Nuevo Stock UD2 y Nueva Fecha Caducidad
Completar el Inventario
En el fichero excel, se debe completar la cantidad de stock a inventariar en el campo Nuevo Stock de cada artículo.
Registrar las cantidades inventariadas
Proceso:
Acude a Inventarios, localiza los artículos / almacenes a inventariar.
Con el listado en pantalla, ejecuta el proceso  Importar Fichero Excel.
Revisa la nueva información mostrada en el dato: Stock.
Para finalizar, ejecuta el proceso  Actualizar Stock.
Efectos:
Los mismos que al realizar un Inventario en el sistema.

Deshacer un inventario
Existen dos opciones, veamos cada una de ellas y sus efectos.
Deshacer Último inventario
Proceso:
Acude a Inventarios
Selecciona los artículos-almacén para los que deseas deshacer el último inventario generado.
Ejecuta el proceso  Eliminar último inventario.
Efectos:
El Artículo-Almacén recupera la información anterior al inventario eliminado.
El sistema genera los movimientos de corrección correspondientes. Para comprobarlo, acude a la Consulta de Movimientos y utiliza el filtro Mostrar Correcciones.
Inicializar Inventarios
Proceso:
Acude a Inventarios
Ejecuta el proceso  Inicializar Inventarios.
Efectos:
Importante: esta acción afecta a todos los Artículos-Almacén registrados en el sistema.
El Artículo-Almacén muestra desactivada la opción Inventariado y la Fecha último inventario queda vacía.

Cierre de Inventarios
En todas las organizaciones resulta fundamental mantener un control económico permanente. Habrá controles específicos de área (compras, ventas, fabricación) pero resulta imprescindible realizar un control global de todas las áreas, lo que se obtendrá, en todos los casos, mediante la obtención del dato “resultado de explotación”, es decir, el valor del beneficio o pérdida acumulado.
Este valor se obtiene siempre desde la contabilidad como operación de: Beneficio de explotación: Ingresos - Gastos + Diferencia de Inventario
Por ello la valoración económica del total de los materiales almacenados en sus diferentes formas, materias primas, producto semielaborado, producto terminado y del material en curso, tiene siempre una repercusión directa y significativa sobre los resultados de explotación (beneficios / pérdidas) de la empresa. El grado de precisión y la periodicidad con la que se extrae la cuenta de explotación depende de cada empresa, pero la práctica habitual es la de periodicidad mensual. Una vez calculado el beneficio o pérdida acumulado a una fecha, este debe permanecer invariable por el curso de las actividades (y por el registro informático de las informaciones) que se desarrollen a partir de esta fecha. Esto significa que se deberá, mensualmente, cerrar cuentas de forma que todos los registros de información no alteren los resultados anteriores a la fecha del último cierre. El sistema informático debe mantener activadas las barreras necesarias para evitar que el resultado de un mes resulte alterado por procesos posteriores. En este informe se describen las condiciones que debe cumplir el sistema para garantizar un cierre contable preciso y fiable. Los cierres de inventario se enmarcan dentro de un proceso más general de cierre contable.
Los cierres contables constan de dos fases:
Cierre de inventarios que consisten básicamente en realizar una valoración de inventario adecuada y el correspondiente asiento contable de diferencia de inventario. Para evitar modificaciones sobre estos datos se cierra el inventario de forma que no se pueda alterar el conjunto de movimientos de almacén utilizados como base para dichos cálculos.
Cierre de cuentas contables que consiste en impedir cualquier tipo de alteración sobre los apuntes contables incluidos en el periodo de cierre correspondiente.
El cierre de los almacenes dentro de un periodo implica una serie de procesos y verificaciones que garantizan que la valoración del almacén es una valoración correcta y que todos los productos almacenados han sido valorados de forma adecuada. En el momento en que se hayan finalizado estos pasos y se hayan verificado uno por uno, el sistema permitirá realizar el cierre del almacén.
Una vez realizado el cierre se podrán contabilizar los resultados obtenidos por medio de un asiento de diferencia de inventario para a continuación efectuar el cierre del diario contable. El cierre de un periodo desde un punto de vista puramente contable implica la asignación de todos los apuntes contables del periodo a dicho cierre y el establecer los sistemas de control adecuados que impidan el registro de nuevos apuntes dentro de dicho periodo. Siguiendo con la misma idea, el cierre de un inventario implica la asignación de los movimientos del periodo al cierre y el control que impida la generación de nuevos movimientos dentro del periodo así como la modificación de los que ya existan.
En esta introducción se ha explicado el proceso general de un cierre contable y las implicaciones del cierre de almacén en el mismo. No obstante se debe de tener en cuenta que habrá situaciones en las que no sea necesario realizar cierres de inventario dado que las existencias se regularizan manualmente.

Configuración Previa
Deberemos indicar si vamos a obligar a realizar el Cierre de inventario.
Proceso:
Acude a Parámetros.
Localiza el parámetro:Obligación de Cierre de Inventario previo Cierre contable (CIERREINV).
Asimismo, existirán procesos de Cálculo de stock a fecha y Valoración de almacén inventario independientes del proceso de cierre de inventarios. En este caso estos procesos tendrán carácter de simulación y los valores obtenidos a través de ellos no tendrán efecto en ningún cierre.

Pasos para realizar el Cierre
El Cierre de stock tiene por objetivo evitar que se registren movimientos dentro de un periodo inventariado y cerrado que puedan alterar el valor del inventario.
Una vez se genere el cierre de un inventario para un periodo no se podrán incluir, eliminar ni modificar movimientos que se encuentren dentro de dicho periodo.
Para realizar el cierre de inventarios debe ejecutar los siguientes procedimientos y en el siguiente orden:
Generar una propuesta de cierre.
Revisar, analizar y ajustar si es necesario la información obtenida.
Realizar el cierre de inventario.
Contabilizar el cierre del inventario.
Trasladar los datos del cierre a la contabilidad mediante la regularización de las existencias.
Importante:
Los procesos de Propuesta de cierre, Cierre de inventario y Contabilización del cierre de inventario se realizan en la misma pantalla “Confirmación de cierres de Inventario”. Sin embargo existe también la pantalla “Confirmación de cierres de Inventario (Nuevo)” que en aspecto y funcionamiento es identica a la anterior, pero ambas difieren en la forma en que se obtienen los datos de la valoración:
Confirmación de cierres de Inventario: para realizar el cálculo de las valoraciones de almacén según un criterio u otro, debemos ejecutar un proceso.
Confirmación de cierres de Inventario (Nuevo): permite obtener los precios reales en el momento actual y sin necesidad de recalcularlos.
¿En qué afecta el uso de una pantalla u otra?
Simplemente deberemos tener en cuenta que para poder utilizar la nueva pantalla debemos tener la información previa de los precios calculados en cada movimiento (histórico de movimientos), si estos campos están vacíos la nueva pantalla no funcionará.

Crear la Propuesta de Cierre
En primer lugar debemos realizar una propuesta para el cierre, de forma que podamos analizar todos los datos que vamos a incluir en el cierre. Antes de realizar la propuesta, debemos debemos tener en cuenta que:
El sistema no dará por correcta la propuesta, si el stock es negativo.
La fecha de la propuesta debe coincidir con la fecha final del periodo.
Veámos cómo desarrollar este proceso:
Acude a Confirmación de Cierre de Inventario.
Indica los datos: Ejercicio y Periodo (obligatoriamente, puede además seleccionar los criterios que requiera de acuerdo a la propuesta que va a realizar).
Vemos que al indicar estos datos, se despliega la siguiente información:
Propuesta Correcta: NO. En este caso, al estar generando la propuesta por primera vez, indica aún no se ha lanzado. Si esto ya se hubiera realizado, un NO indicaría que la propuesta lanzada no ha sido correcta.
Cerrado: NO. No se ha realizado el cierre del periodo.
Contabilizado: NO. No se ha contabilizado el cierre.
Ejecutamos la búsqueda pulsando sobre el botón de prismáticos, o bien F5. No se mostrará ningún resultado ya que la propuesta no se ha lanzado aún.
Ejecutamos el proceso  Propuesta de Cierre. Al estar realizando el proceso por primera vez, será la única opción de el botón de procesos que podremos seleccionar.
Indicamos los datos de la propuesta:
Por defecto se muestran los datos recogidos previamente en los criterios de selección: Ejercicio, Periodo, estado de la Propuesta, Cierre y Contabilización.
Podremos seleccionar si queremos incluir los artículos obsoletos dentro de nuestra propuesta y posterior cierre de Inventario.
Nota: un artículo obsoleto es aquel que aunque tenemos registrado en el sistema, no se encuentra activo. El Estado que determina si un artículo está obsoleto, es aquel que independientemente de su nombre y definición, no tiene activada la marca de ☑ Activo.
El sistema nos informará cuando la propuesta se haya realizado:
En caso de ser correcta, únicamente informa del fin del proceso, pulsamos “Aceptar” y continuamos.
En caso de que la propuesta tuviera un fallo, el sistema nos indicaría que el proceso está en curso además del motivo por el cual la propuesta no ha sido correcta. Procederíamos entonces a realizar los ajustes necesarios para corregir la propuesta (Siguiente punto: Realizar Ajustes).
Nota: Por lo regular un fallo se da cuando existen stocks negativos de un artículo.
Un stock negativo es únicamente posible en casos especiales: se debe indicar expresamente mediante parámetros que se requiere gestionar stocks negativos, esto nos permitirá realizar salidas de mercancía aun cuando no las tenemos registradas dentro de un almacén en el sistema.
El parámetro para la gestión de stocks negativos es “STNEGATIVO | Stock Negativo: Control General” 1 = Activada | 0 = Desactivada.
Finalmente podemos ver en pantalla:
El listado de artículos inventariados según los criterios establecidos.
El almacén en el que se encuentra cada artículo (se muestra una línea de cada artículo por cada almacén).
El stock en nuestro almacén para el periodo que hayamos indicado (Stock a Fecha) así como el stock a la fecha en la que estamos lanzando el proceso (Stock Actual).
En la columna “Precio Almacén” se muestra el precio del artículo según su criterio de valoración. Puede ser bien el criterio correspondiente al artículo (artículo > apartado Almacenes > criterio de valoración) o bien el calculado como criterio de valoración en proceso de valoración de almacenes. De cualquier forma usted podrá saber qué criterio se está utilizando para cada artículo ya que se mostrará coloreado en amarillo el precio correspondiente al Criterio que se esté utilizando: medio, FIFO, Ultima Compra, etc.
Si desea calcular el precio y con un criterio diferente, seleccione las líneas a recalcular y ejecute el proceso  “Nuevo Criterio de Valoración”.
La columna “Valor A” muestra el valor total del almacén teniendo en cuenta: (Stock a Fecha * Precio de Almacén). Siendo el Precio Almacén el precio según el criterio de valoración del artículo (el que se encuentre en marcado con color, se recoge y se lleva a la columna “Precio Almacén”).
En las columnas: “Precio Estándar”, “Precio FIFO (Fecha)”, “Precio FIFO (Movimiento)” y “Precio Medio”, se muestra el precio del artículo según el criterio correspondiente.
La fecha en la que se realiza el cálculo de la valoración (Fecha Cálculo).
Cuando la propuesta ha sido completada correctamente:
Se muestra como: Propuesta Correcta: SI.
En el mantenimiento de “Cierres de Inventario” se muestra la línea correspondiente al periodo de la propuesta con la opción ☑ Propuesta Correcta activa. (Debe seleccionar la solapa correspondiente al ejercicio).
Cada vez que genere una nueva propuesta se irá generando una nueva línea.
Al momento de realizar el cierre se activa la marca ☑ Cerrado Inventario.
Una vez obtenida la propuesta, puede realizar los ajustes que requiera, tal y como se describe acontinuación. De no ser así continue con al cierre de inventario.

Realizar ajustes a la propuesta
Al ejecutar la propuesta de cierre el sistema obtiene automáticamente el stock existente y su valoración (información es obtenida de los datos registrados en el  histórico de movimientos). Sin embargo es posible modificarla en caso de ser necesario.
Utilizando las pantallas de “Ajustes”, “Movimientos manuales” o bien realizar correcciones en el inventario, podremos modificar el stock físico de nuestros almacenes. Tenga en cuenta que:
Uno de los ajustes que podríamos llegar a realizar es por stock negativo, ya que la propuesta se considere válida el sistema verifica que no haya ningún artículo con stock negativo. Este caso es algo inusual pero existen puede presentar esta situación en los siguientes casos:
Por acumulación de errores en procesos de descuento automático: en aquellos procesos en que se descuenten materiales por medio de procesos automáticos se va acumulando un error que puede desembocar en un stock negativo. Estos errores se pueden originar debido a que las cantidades a descontar se calculan en función de la estructura de cada artículo y la utilización del dato de la merma hace que se vaya acumulando un error.
Por la existencia de albaranes de entrada sin actualizar: en estos casos se comienza a dar salida a producto que existe en el almacén, físicamente, pero sin que los albaranes de entrada correspondientes hayan sido actualizados, por lo que el sistema no está ‘informado’ de la entrada.
Después de realizar los ajustes necesarios procederemos a realizar el proceso  “Recalcular Stock y Precios a Fecha”, que le permite ver las modificaciones del stock realiza los cálculos para su valoración.
Nota: haciendo click derecho sobre las líneas, podrá realizar las siguientes operaciones
Ver Artículo.
Recalcular Stock y Precios a Fecha.
Mostrar Detalle Stock a Fecha.

Cierre de Inventario
Proceso:
Para realizar el cierre puedes:
En Confirmación de Cierre de Inventario: indica los datos del Ejercicio / Periodo a cerrar y ejecuta la búsqueda.
En Cierres de Inventario: selecciona la pestaña del ejercicio, la línea de la propuesta, pulsar el botón secundario y seleccionar “Mostrar Detalle”.
Ejecuta el proceso Cierre de Inventario
Comprueba los datos y pulsa Aceptar.
Se realiza una valoración del inventario para un periodo determinado. Ten en cuenta que:
La fecha de cierre debe coincidir con la fecha final del periodo.
No se puede cerrar un periodo sin haber cerrado antes el periodo anterior.
No puede deshacer el cierre de un periodo, si los periodos posteriores están cerrados.
Una vez realizado el cierre, éste podrá ser contabilizado para a continuación lanzar el cierre contable de las cuentas.
El cierre sólo se realizará si se han superado las fases anteriores.
El sistema informa que se ha finalizado el proceso. Si acudes a Cierres de Inventario, verás que la línea de la propuesta ya se muestra como Cerrado inventario y con la fecha en la que se realizó el proceso.
Si por alguna razón se desean incluir nuevos movimientos dentro del periodo cerrado, será necesario borrar el cierre (deshacer el cierre) introducir la nueva información. Y posteriormente volverlo a crear.

Deshacer Cierre de Inventario
Para realizar este paso se requiere que el cierre no esté contabilizado.
Proceso:
En Confirmación de Cierre de Inventario ejecutamos el proceso  Deshacer Cierre.
Este proceso implica que todos los movimientos asociados al mismo volverán a estar en disposición de ser modificados (tendrán la marca de Cerrado a No) y que se podrán insertar nuevos movimientos.

Contabilizar Cierre de Inventario
Proceso:
En Confirmación de Cierre de Inventario ejecutamos el proceso  Contabilizar Cierre.
Se genera un asiento de Diferencia de inventario que al contabilizarse impide cualquier tipo de alteración sobre los apuntes contables incluidos en el periodo de cierre correspondiente.

Descontabilizar Cierre de Inventario
Proceso:
En Confirmación de Cierre de Inventario ejecutamos el proceso  Descontabilizar Cierre.

Regularización de Existencias
Este proceso permite trasladar los datos obtenidos en el cierre de inventario a nuestra contabilidad. Antes de iniciar el proceso de regularización deberemos revisar el parámetro:
Valoración de almacen para la Regularización de Existencias (VALALM): Si este parámetro está a verdadero, para los saldos finales de asiento de regularización de existencias, se propone el valor del Cierre de Inventario cuya cuenta de CCStocks sea la de origen. El usuario podrá modificarlo en el propio proceso.
Partimos de artículos, cantidades e importes, como a cada artículo se le asocia una cuenta de Stocks el proceso es directo.
Parametrización de la Regularización de Existencias
Esta pantalla se utiliza para rellenar la información relativa a la ‘Regularización de Existencias’, su contenido sólo será modificable cuando se establezca un nuevo plan general contable ya que la especificación de las cuentas que intervienen en dicha regularización viene determinada por el propio Plan Contable.
Sabiendo las existencias iniciales, suma de los saldos de las cuentas definidas; el asiento al que van a pasar (destino) y las existencias finales que son las calculadas en el último cierre, el proceso de contabilización será automático dejando únicamente abierta la opción de posibles cambios manuales de cuentas que no estén definidas en el cierre de inventario.
La longitud de las cuentas origen y destino será de 3 dígitos, no se permiten más.
Regularización de Existencias
Consiste en trasladar los datos obtenidos anteriormente a fin de gestionar contablemente los cierres de inventario.
Se mostrarán los resultados de enfrentar la tabla de parametrización de la Regularización de Existencias con la de Cierre de Inventario y el Diario Contable.
Fecha: por defecto, coge la fecha actual.
Ejercicio: indicamos el ejercicio para la regulación.
Último cierre: indicamos el periodo del ejercicio. Debe estar “Cerrado”.
Una vez cumplimentados los datos anteriores, se ejecutará el proceso  Calcular Regularización.
Si existen más de un cierre sin contabilizar, aparecerá un mensaje de advertencia.
Una vez realizado el proceso, aparecerá la información resultante en pantalla.
Podemos, posteriormente, manipular estos datos si es que aparece alguna existencia que no existe en Inventarios.
Una vez realizado el proceso anterior, procederemos a su contabilización, para ello ejecutaremos otra acción Contabilizar Cierre.
Genera un asiento de regularización de existencias.
Este asiento generará 4 apuntes:
Si la parametrización de la contabilidad analítica de nuestra aplicación está indicada “Por artículo” (Origen de la asignación analítica | 1 AA por Artículo) obtendrá el desglose pulsando sobre el icono  de cada línea.
Tras la aceptación de esta contabilización cambiará el estado del periodo seleccionado a “Contabilizado”.
Al cierre del ejercicio se deberá realizar la regularización de existencias (en caso de no llevar un sistema de inventario permanente) y se debe traspasar al balance el valor de las existencias finales, calculadas por algún método aceptado, reconociendo en resultados la diferencia entre las existencias finales e iniciales.

Actualización de Documentos posteriores al Cierre
En caso de que haya algún cambio en los importes en documentos (albaranes o facturas) cuyos movimientos se encuentren dentro de un periodo ya cerrado, el sistema actuará de la siguiente manera:
Generará movimientos de corrección que compensen aquellos movimientos que se vean involucrados.
Se genera un nuevo movimiento con fecha igual a la fecha de la factura y con los nuevos datos de valoración. En caso de que la fecha de la factura también esté dentro del periodo de cierre, se le asignará como fecha el primer día del primer periodo abierto.

Gestión por Punto de Pedido
La actividad de almacenar existencias, en muchos casos, viene motivada por el hecho de que los aprovisionamientos no suelen ser instantáneos. Es normal que medie un tiempo inevitable entre el momento en que se hace un pedido y el instante en que las existencias correspondientes a dicho pedido llegan al almacén.
Por ello se ha de hacer el pedido cuando las existencias en almacén sean suficientes para atender la demanda durante este plazo de reposición. Al nivel de existencias que define este instante en que se ha de hacer el pedido lo llamamos punto de pedido.
El punto de pedido es el nivel de disponibilidad total o neta que indica la necesidad de solicitar inmediatamente al departamento de compras la tramitación de un nuevo pedido.
Punto de pedido = demanda durante el plazo de la entrega/fabricación + stock de seguridad.
La aplicación está preparada para poder realizar una planificación del aprovisionamiento, según necesidades de compra o de fábrica, en función del punto de pedido.
Asignar el Punto de Pedido
Si deseas gestionar el punto de pedido para una referencia debes identificarlo en: Artículo-Almacén.
Proceso:
Acude a Artículos y localiza la referencia.
En el apartado Almacenes, localiza el almacén (el punto de pedido se establece para artículo y almacén)
Activar la opción ☑ Punto de Pedido e indica la cantidad, considerada en Unidad interna, en el dato Punto de Pedido.
Posteriormente podrás planificar el aprovisionamiento (compras u órdenes de fabricación) teniendo en cuenta el valor del punto de pedido.
Actualizar el Punto de Pedido
Para actualizar de forma masiva la cantidad de punto pedido establecida para cada uno de los artículos-almacén registrados.
El sistema cuenta con una serie de operaciones que permiten generar resultados a partir de las operaciones registradas, tanto de Compra como de Fabricación:
Calcular según las Compras
El sistema realiza el siguiente cálculo:
Para cada uno de los artículos y almacén asociado, se revisan los movimientos de entrada del último año. Se obtiene el ‘Consumo Mensual’ (= Consumo anual / 11) y, se multiplica por el ‘Plazo de Compra’ para obtener el punto de pedido de un artículo a comprar.
Movimientos de entrada del último año > Consumo Anual > Consumo Mensual = Consumo Anual / 11
Punto de Pedido =  (Consumo Mensual / 30) * Plazo de Compra.
Calcular según la Fábrica
El sistema realiza el siguiente cálculo:
Para cada uno de los artículos y almacén asociado, se revisan los movimientos de entrada del último año. Se obtiene el ‘Consumo Mensual’ (= Consumo anual / 11) y se multiplica por el ‘Plazo de Fábrica’ para obtener el punto de pedido de un artículo a fabricar.
Movimientos de entrada del último año > Consumo Anual > Consumo Mensual = Consumo Anual / 11
Punto de Pedido = (Consumo Mensual / 30) * Plazo Fábrica.
Proceso:
Acude a Actualización Punto de Pedido.
Selecciona las líneas a actualizar.
Elige la Operación a realizar:
Calcular según las compras.
Calcular según la fábrica.
Modificando de forma manual: al seleccionar esta opción el sistema habilita el campo ‘Plazo’ para cada una de las líneas de artículos, en este campo puede introducir uno a uno, el plazo para cada artículo.
Aplicando un valor: al seleccionar esta opción el sistema habilita el campo ‘Plazo’, en este campo puede introducir el valor del plazo de punto de pedido que va a imputar a todos los artículos seleccionados
Ejecuta el proceso  Actualizar Punto de Pedido.

Planificación bajo Punto de Pedido
La aplicación, a través de esta pantalla de tipo consulta interactiva , presentará las necesidades de compra o fabricación para aquellos artículos que hayan sido identificados con la marca ‘Punto de Pedido’.
Permitirá lanzar de forma masiva los correspondientes Pedidos, Solicitudes de Compra o Programas (para los artículos de tipo “compra”) o bien las correspondientes Órdenes de Fabricación (para los artículos de Tipo Fábrica) de los artículos cuyas necesidades así lo dispongan.
Datos:
Artículo y Descripción: Código y Descripción del Artículo.
Almacén: asociado al artículo.
Stock Seguridad: stock mínimo que deseamos tener almacenado.
Stock Físico: stock real en Almacén.
En Curso: el sistemarecoge las cantidades provenientes tanto de los Pedidos de Compra en curso (Q1)como de los Programas registrados (Q2), como de las Órdenes de Fabricación lanzadas (Q3), realizando el siguiente cálculo:
Q1: recogerá aquellas líneas cuyo estado sea distinto de “Servido” o “Cerrado”, en éstas calculará:
Si la Cantidad Pedida es mayor que la Cantidad Servida, entonces Q1 = C. Pedida –  C. Servida.
Si la Cantidad Pedida es menor que la Cantidad Servida, entonces Q1 = 0.
Q2: cantidad Programada – Cantidad Confirmada.
Q3: recogerá aquellas líneas cuyo estado sea distinto de “Terminada” o “Anulada”, en éstas calculará:
Si la Cantidad a Fabricar es mayor que la Cantidad Fabricada, entonces Q3 = C. a Fabricar –  C. Fabricada.
Si la Cantidad a Fabricar es menor que la Cantidad Fabricada, entonces Q3 = 0.
De los cálculos anteriores, se dará el siguiente resultado: En Curso = Q1 + Q2 + Q3
Punto Pedido: cantidad del  Punto de Pedido, para aquellos artículos con Gestión de Punto de  Pedido.
Diferencia: cantidad resultante del cálculo:
(Stock Físico +   En Curso)  –  Cantidad Punto Pedido.
Si el campo Diferencia muestra un valor negativo, indica que se ha de lanzar un Pedido de Compra (si se trata de un artículo de tipo Compra) o bien,  una Orden de Fabricación (si se trata de un artículo de tipo Fábrica).
Lote Mínimo: Lote mínimo de fabricación o de compra.
Los criterios de selección predeterminados son:
Artículo, Tipo, Familia, Subfamilia, Diferencia < (menor que).
Fabricado – Comprado: incorpora un enumerado en el que las opciones son:
Fabricado: artículos cuyo Tipo asociado tiene la marca de “Fábrica”.
Comprado: artículos cuyo Tipo asociado tiene la marca de “Compra”.
Todos.
Los Procesos disponibles son:
Generar Pedidos de Compra
Generar Órdenes de Fabricación

Gestión de Stock de Seguridad
También llamado stock de protección, lo podemos definir como el volumen de existencias que se tiene en el almacén, por encima de lo que normalmente se espera necesitar, para hacer frente a las fluctuaciones en exceso de demanda o a retrasos imprevistos en la entrega de los pedidos.
La aplicación permite el uso de este stock de seguridad en su planificación MRP tanto de Compras como de Fabricación.
Si desea gestionar el stock de seguridad para una referencia, debe acudir a su ficha de artículo y en la solapa de Almacenes localizar el almacén (el stock de seguridad se establece para artículo y almacén) e indicar la cantidad (en ‘unidad interna’) en el dato ‘Stock de Seguridad’.

Gestión de Lote Mínimo de Fabricación
Permite establecer la cantidad mínima por lote de fabricación independientemente de la necesidad a fabricar.
Lote Mínimo: Indica la cantidad de lote mínimo a fabricar o comprar. Este dato se establece en la relación Artículo - Almacén, esto es, se indicará un lote mínimo para cada uno de los almacenes que tenga asociado el artículo. Por lo que este dato se cumplimentará en la solapa almacenes del mantenimiento de artículo.
El sistema permite la actualización masiva de los Lotes mínimos establecidos para cada uno de los artículos registrados.
Proceso:
Acude a Actualización de Lotes Mínimos,
Selecciona los registros.
Selecciona la Operación a realizar.
Modificando de forma manual: introduce un valor en el campo Nuevo Lote Mínimo de cada línea seleccionada.
Aplicando un valor: actualiza todas las líneas seleccionadas con el mismo valor de Lote Mínimo. Al seleccionar ésta aparecerá un nuevo campo Lote Mínimo, donde se insertará el valor a otorgar al lote mínimo de cada una de las líneas seleccionadas.
Ejecuta el proceso:  Actualizar Lote Mínimo.

Gestión de Stock Negativo
La Gestión de Stocks Negativos nos permite dar salida a artículos, aun cuando el sistema indique que no tenemos stock disponible. Esta gestión conviene en casos como por ejemplo:
Tenemos stock físico en nuestro almacén, sin embargo este no ha sido actualizado por el encargado.
No tenemos stock físico en nuestro almacén, sin embargo hemos asegurado una recepción de mercancía por parte de proveedor regular para antes de la fecha de entrega de nuestro pedido.
En ambos ejemplos, podríamos surtir los pedidos (reflejar la salida de producto de almacén en el sistema) si trabajamos con la Gestión de Stock Negativo.
Para trabajar con los stocks negativos, primero deberemos determinar cómo vamos a trabajar, esto es porque el sistema permite tres formas de trabajo:
Stock Negativo General: Todos nuestros artículos se gestionan con Stock Negativo.
Stock Negativo por Artículo: Solo los artículos que indiquemos se gestionarán con Stock Negativo.
Sin gestión de stock: Ningún artículo se gestiona con Stock Negativo.
Nota: recordemos que el sistema permite trabajar con artículos cuyo stock no nos interesa gestionar, es decir no controlamos su stock. En este caso obviamente no se gestionará tampoco el stock negativo (sea cual sea la forma de trabajo que hayamos establecido para el stock negativo). Por ello debemos prestar especial atención en cómo están configurados nuestros artículos y estar seguros de cuáles tienen gestión de stock.

Stock Negativo General
En este caso vamos a parametrizar la aplicación para que todos nuestros artículos con gestión de stock permitan stocks negativos.
Proceso:
Acudiremos al mantenimiento o consulta de parámetros, desde donde localizaremos y activaremos el parámetro "STNEGATIVO | Stock Negativo: Control General.", indicando el valor: Si | 1.
Al activar este parámetro se habilita la gestión de stocks negativos para todos los artículos con gestión de stock, sin ninguna restricción.

Stock Negativo por Artículo
En este caso vamos a parametrizar nuestra aplicación para que solo los artículos que especifiquemos puedan gestionarse con Stocks Negativos.
Para esta forma de trabajo, el sistema realizará tres comprobaciones:
Para la primera comprobación, indicaremos al sistema que no queremos trabajar con stocks negativos para todos los artículos (lo opuesto al apartado anterior), para ello:
Acudimos al mantenimiento o consulta de parámetros, localizamos el parámetro "STNEGATIVO | Stock Negativo: Control General" y lo desactivamos indicando el valor: No | 0.
Para la siguiente comprobación, indicaremos al sistema que queremos permitir el Stock Negativo para algunos artículos (que especificaremos más adelante).
Acudimos al mantenimiento o consulta de parámetros, localizaremos el parámetro "ST_NEG_ART | Stock Negativo: Control por Artículo" y lo activamos indicando el valor: Sí | 1.
La última comprobación será ver qué artículos son los que gestione con Stock Negativo.
Acudimos al mantenimiento del artículo que queremos gestionar con Stock Negativo.
Nos posicionamos en la solapa "Almacenes" y activamos la marca "☑ Permitir Stocks Negativos".
Repetimos esta operación en las fichas de todos los artículos que vamos a gestionar con Stocks Negativos.

Sin Stock Negativo
Para ello, el sistema realizará dos comprobaciones:
Que no queremos trabajar con el stock negativo general. Para indicar esto:
Acudimos al mantenimiento o consulta de parámetros, localizamos el parámetro "STNEGATIVO | Stock Negativo: Control General" y lo desactivamos indicando el valor: No | 0.
Que tampoco queremos trabajar con stock negativo por artículos.
Acudimos al mantenimiento o consulta de parámetros, localizaremos el parámetro "ST_NEG_ART | Stock Negativo: Control por Artículo" y lo desactivamos indicando el valor: No | 0.

Gestión de Lotes
Permite gestionar Lotes de Fabricación o Compra, identificando los distintos códigos de lote en cada uno de los procesos que acometa: la cantidad de artículo por lote, la ubicación del lote así como su fecha de caducidad.

Consulta de la Trazabilidad de un Lote
Esta herramienta le permitirá localizar todos los artículos/lotes relacionados con el lote que se consulta: las entradas, salidas y el stock actual.
Proceso:
Acude a Trazabilidad Lote.
Indica el Artículo y el Lote.
Efectos: el sistema muestra los datos de:
Origen
Entradas en las que ha intervenido ese lote o algún componente de ese lote.
Si el material se ha comprado se identificará el albarán de compra, fecha, proveedor, …
Destino
Salidas en las que ha intervenido ese lote.
Si es un albarán de venta (multinivel) identificar numero, fecha, cliente, .. Si es una OF identificar numero, fecha,...
Stock
Lista de artículos, lotes y ubicaciones que están actualmente en el almacén donde se haya incorporado ese lote en algún nivel de su producción o stock de ese lote del propio artículo.

Gestión de Números de Serie
Tendrá identificados todos los números de serie de cada unidad de artículo así gestionado. El sistema reconocerá las referencias que requieren de esta identificación adicional, y le solicitará de forma automática que indique el número de serie correspondiente tanto en la recepción como en la expedición de mercancía e incluso durante su incorporación en los procesos productivos.

Gestión de Envases retornables
A continuación detallamos cómo configurar y manejar la gestión de los envases retornables (o embalajes retornables), esto es, controlar los envases en los que expide la mercancía de forma que pueda gestionar la devolución de los mismos.
Registro de Embalajes y Envases
Clasificar los embalajes/envases retornables
Debemos configurar un Tipo de artículo que específico para clasificar los Embalajes y los Envases retornables.
Esto es que debe estar activada la opción ☑ Embalaje.
En caso de que trabaje con la gestión de fabrica, ha de tener también la opción ☑ Fábrica para poder utilizar los embalajes/envases en el circuito de fabricación.
Alta de un embalaje / envase retornable
Todos los embalajes se registran al igual que nuestros productos, en el mantenimiento de Artículos, la forma de diferenciarlos es indicando el tipo de artículo correspondiente al Embalaje, configurado en el paso anterior.
Crear los almacenes para devoluciones de envases
Utilizaremos el Almacén para identificar que un embalaje / envase se encuentra en destino y que debe ser devuelto. Por ello en el mantenimiento de almacenes, registraremos los almacenes "contenedores", teniendo en cuenta las siguientes consideraciones:
El almacén para devolución de embalajes es un dato de maniobra que nos permite llevar a cabo la devolución, por lo que puede ser real o ficticio. Podemos  identificar un almacén para cada Cliente o bien un único almacén que identifique de forma genérica. Por ejemplo creamos un almacén genérico para las devoluciones: "Destino Cliente (devolución)".
Los almacenes para devolución de embalajes se consideran ‘Propios’ ya que las existencias en ellos ubicadas, deben tratarse en la valoración de almacenes y / o en los cierres contables de almacén.
En la ficha del cliente debemos indicar el Almacén para devoluciones en el campo "Almacén Contenedor" .
Asociar el embalaje a los artículos
En este paso lo que hay que hacer es ir a la ficha de nuestros artículos (productos) e indicar para cada uno de ellos cuál es el artículo-embalaje correspondiente:
Acudimos a la ficha del artículo-producto.
Acudimos al apartado Unidades y Precios e indicamos el embalaje que le corresponde a ese artículo en el campo Tipo Contenedor.
Por ejemplo indicamos el embalaje que registramos en el paso anterior "Alta de un envase retornable": 0000000777 | Caja. De esta forma ya sabemos que cuando realicemos una venta del artículo Bieleta Montada, este se embalará en Cajas y para estas se mantendrá el registro de envios a almacén de envases retornables, como veremos mas adelante.

Gestión de Envases retornables
Expedición del Envase
Con los datos anteriores el sistema se encarga de en cada expedición (albarán de venta) de ver si el cliente tiene un almacén contenedor y trasladar a éste todos los envases implicados realizando el correspondiente movimiento de salida de stock de envases a la vez que hace la salida de stock de la mercancía del almacén del envío.
Devolución del Envase
Posteriormente conforme se vaya dando la devolución de envases, acudiremos Envases Retornables, localizaremos el cliente y procederemos a indicar la cantidad de envases devueltos, con lo que el sistema realizará de nuevo el movimiento de stocks de entrada al almacén de origen de los envases.
Consultar Estado envases
En Envases Retornables podemos realizar consultas tales como: cuántos envases tiene acumulados determinado cliente, etc.

Gestión Avanzada de Embalajes
El aspecto relevante de la gestión avanzada de embalajes reside en obtener una Declaración de Embalajes utilizados en la expedición.
La definición y configuración de los embalajes utilizados en las expediciones comienza con la definición del Tipo y Familias de Embalajes.
El sistema interpreta tres grandes grupos de clasificación:
Embalaje: aquellos que incluyen unidades de artículos y que van dentro de un contenedor. Ejemplo: Caja con 12 unidades de producto.
Contenedor: aquellos que incluyen unidades de embalajes o bien, directamente, unidades de artículos. Ejemplo: Palet con 6 Cajas (cada una de ellas, con 12 unidades de Producto).
Componente adicional: aquellos que participan del embalaje y que es necesario informar cuando utilizamos el sistema EDI para trasladar la información de la expedición (representada en el documento del albarán de venta). Ejemplo: Tapas de Palet.
Parametrización
Para poder utilizar la gestión avanzada de embalajes debemos tener activado el parámetro: Gestión avanzada de Embalajes (GESTEMB).
Nota: En una gestión "sencilla" de embalajes, con definir los Embalajes y Contenedores sería suficiente para gestionar los embalajes en la preparación de la expedición.

Definir los Embalajes (Palets, Contenedores, Cajas...)
Necesitaremos crear un Tipo de artículo para configurar los distintos embalajes y elementos que utilicemos en la preparación de la expedición. En ocasiones será necesario informar en el desglose del albarán, de los componentes que forman parte del embalaje: palets, contenedores, cajas, separadores, foams, flejes, etc.
Definir el Tipo Embalaje
Proceso:
Acude a Tipos de Artículos.
Crea un nuevo registro con el nombre, por ejemplo: Embalajes.
Activa la opción ☑ Embalaje.
Sin olvidar otras opciones necesarias para la gestión de la Logística en Solmicro ERP. Por ejemplo: ☑ Compra (si se adquieren), y/o ☑ Fábrica (si se fabrican internamente o participan de algún proceso de fabricación), ☑ Stocks y
Definir las Familias de embalajes
Proceso:
Acude al Tipo = Embalajes, creado en el proceso anterior.
Crea tantas Familias como desees configurar, por ejemplo: Cajas, Palets, Separadores, etc... activando las siguientes opciones:
Embalajes que no van dento de otro embalaje = ☑ Contenedor. Ej.: Palets
Embalajes que van dentro de otro embalaje = ☑ Embalaje. Ej.: Cajas (que se incorporan al Palet)
Elementos que se deben informar en los ficheros EDI y que participan de los embalajes = ☑ Componente Adicional. Ej.: Tapa del Palet.
Otros elementos que participan del embalaje y no son ninguno de los anteriores pero necesitamos controlar su stock, no es necesario activar ninguna opción. Ej.: Separadores de las cajas, Foams.
Datos:
Los datos a definir serán distintos en función de cómo participan los embalajes entre sí, existen distintos casos:
Cajas que van "sueltas" = Contenedor.
Cajas que van en un palet u otra Caja mayor = Embalaje.
Definir los Embalajes
Tras la clasificación de los Embalajes debemos definir cada una de las referencias de los embalajes como artículos del sistema.
Debemos definir un artículo para la caja de cartón (EMBC01) 20x30x40, otro para la caja de cartón (EMBC02) 40x50x50, otro para el palet de madera (EMBP01) 100x100, otro para el separador de cajas (EMBS01 (EMBC01)) 20x30x2, etc...
Proceso:
Acude al Artículos.
Crea un Artículo por cada Tipo/Familia para definir cada una de las referencias que utilices como embalaje.

Definir la estructura del embalaje
Veamos cómo definir los embalajes en los que se prepara un artículo de venta. Debemos definir cada una de las posibles formas en las que se puede expedir el artículo principal (venta).
Proceso:
Acude al Artículo.
Ejecuta el proceso  Embalajes.
Indica un nombre para el embalaje del artículo, por ejemplo: Embalaje General.
Indica el número de piezas mínimo que debe ir en un embalaje. El sistema utilizará esta cantidad para definir la correspondencia con los Embalajes (Embalajes y/o Contenedores).
Introduce/revisa la información de los componentes del embalaje.
Cantidad: unidades de embalaje necesarias para las piezas por embalaje.
Piezas por Embalaje: por defecto, la cantidad de lote mínimo.
Recoge el componente e indica el total de unidades que incorpora.
Ejemplo: en una caja se incluyen 12 unidades del artículo y en un palet se incluyen 6 cajas. Caja: 12 unidades y Palet: 72 unidades.
El sistema, por defecto, asocia la opción ☑ Principal. Permite distinguir ésta de otras opciones alternativas de embalaje.

Embalaje Principal y embalajes Alternativos (por Artículo y por Artículo/Cliente)
Definir el embalaje Principal y embalajes Alternativos por artículo
Debemos definir cada una de las posibles formas en las que se puede expedir el artículo a expedir (Embalajes por Artículo).
De todas estas posibilidades, debemos identificar una de ellas como Principal, quedando el resto como Alternativas. Para crear nuevos posibles embalajes crearemos un nuevo registro de embalaje por artículo. Una vez definidas, podemos visualizar la información de todas ellas en la búsqueda avanzada de Embalajes por Artículo.
Definir el embalaje Principal y embalaje Alternativo por artículo para determinado cliente
El sistema permite definir el embalaje principal y un embalaje alternativo en función del Cliente y para un Artículo concreto.
Proceso:
Acude al Artículo, apartado Clientes.
Indica el Cliente e identifica su embalaje:
Embalaje principal
Embalaje alternativo

Proceso de Venta y Expedición
El aspecto relevante de la gestión avanzada de embalajes reside en obtener una Declaración de Embalajes utilizados en la expedición.
Pedido de Venta
Proceso:
En Pedidos de Venta, creamos un nuevo pedido.
Indicamos el Cliente y los Artículos en las líneas de pedido.
El sistema completa la información del Embalaje Principal y el Embalaje Alternativo.
Si deseas asociar el Embalaje Alternativo al Pedido, activa la opción de la línea de pedido: ☑ Alternativo.
Efectos:
Si se ha definido un embalaje particular para el cliente, se traslada a la línea del pedido tanto éste como el alternativo.
En caso contrario, el sistema propone el Embalaje principal del Artículo.
En la línea de Pedido aparece un nuevo botón de control  Embalajes: permite acceder a la información del desglose del embalaje, mostrando la cantidad necesaria de cada componente para expedir la cantidad indicada en la línea del pedido.
Albarán de Venta
Proceso:
En la fase de expedición en el Albarán de Venta se muestra la cantidad servida.
En el control de  Embalajes se actualiza la información para mostrar la cantidad de componentes ajustada a la cantidad servida.

Consultas de Embalajes
Permite visualizar las necesidades de embalajes para todos los pedidos de venta en un rango de fechas seleccionado, para identificar próximas
Podemos agrupar por componentes y conocer las cantidades totales netas para poder servir todos los pedidos.

Gestión de Almacenes de Doble Unidad
Esta funcionalidad permite gestionar nuestro stock en dos unidades de medida entre las cuáles no haya un factor de conversión determinado. Un ejemplo de la aplicación de esta funcionalidad podría ser el almacenamiento de ciertos alimentos que requieren ser gestionados en kilogramos y piezas. Aunque la primera medida será la que dará valoración al almacén (kg), la segunda unidad permitirá saber el número de piezas existentes en el almacén. Igualmente en ciertas ocasiones el peso de un alimento puede variar durante su almacenamiento con lo que el controlar las unidades nos permitirá saber si ha habido pérdidas o excedentes de material.
Nota: Si la relación entre las 2 unidades de medida tuviera un factor de conversión fijo  se podría calcular en cada momento tal y como se presenta en Consulta Stock Doble Unidad.

Configuración previa
Parámetros
El primer paso que debe de dar para trabajar con un almacenes con doble unidad es activar el parámetro Gestión de Stock con Doble Unidad.
Proceso:
Acude a Parámetros.
Localiza el parámetro: STOCK2UD | Gestión de Stock con Doble Unidad.
Activa el parámetro, seleccionando el valor = Sí.
Indicar los artículos con Gestión de Doble Unidad
No todos los artículos se gestionarán con doble unidad, únicamente aquellos que indiquemos.
Para indicar qué artículos se va a gestionar con doble unidad, deberá registrar la segunda unidad de medida en la ficha de cada artículo:
Mantenimiento de Artículo > Solapa Unidades / Precios.
Indicamos la segunda unidad en el campo “Ud. Interna 2”, en la ficha de cada artículo.
Una vez indicado este dato, en todos los procesos de los circuitos de ventas y compras en los que intervengan estos artículos se deberemos indicar el valor de la segunda unidad.

En el Circuito de Compras
Pedidos de Compra
Se muestran el campo de la segunda unidad, aunque su registro no es obligatorio para generar el pedido, no podrá generarse la recepción de mercancía sin este dato (ni sea generando albarán desde el pedido ni mediante el proceso de recepción).
Proceso de Recepción de Pedidos
Cuando realicemos el proceso de recepción de un artículo de doble unidad, se mostrará la segunda unidad indicada en el pedido (puede modificarla según lo que reciba, el pedido se completará cuando se alcance la primera unidad en su totalidad). Si la segunda unidad no se ha indicado en el pedido, debe de registrarse en el proceso de expedición, de lo contrario el sistema no permitirá generar el albarán.
Albarán de Compra
Los albaranes generados desde el circuito de compras, tendrán ya toda la información requerida sobre la gestión de la doble unidad. Para albaranes generados fuera del circuito (desde 0) y con gestión de doble unidad, el sistema obliga el registro de dicho valor para poder crearlo.
Nota: todos los albaranes generados son contabilizados al momento de su generación, esto es debido al proceso de Inventario permanente, el cual registra contablemente el incremento de coste de stock y suma el adeudo en las facturas por pagar. 
Factura de compra
Los albaranes generados desde el circuito de compras, tendrán ya toda la información requerida sobre la gestión de la doble unidad.

En el Circuito de Ventas
Pedido de Venta
Se muestran el campo de la segunda unidad, aunque su registro no es obligatorio para generar el pedido, no podrá generarse la expedición de mercancía sin este dato (ni sea generando albarán desde el pedido ni mediante el proceso de expedición).
Proceso de expedición de Pedidos
Cuando realicemos la expedición de un artículo con gestión de doble unidad se mostrará la segunda unidad indicada en el pedido (el pedido se completará cuando se alcance el valor de la primera unidad en su totalidad). Si la segunda unidad no se ha indicado en el pedido, debe de registrarse en el proceso de expedición, de lo contrario el sistema no permitirá generar el albarán.
Albarán de Venta
Los albaranes generados desde el circuito de ventas, tendrán ya toda la información requerida sobre la gestión de la doble unidad. Para albaranes generados fuera del circuito (desde 0) y con gestión de doble unidad, el sistema obliga el registro de dicho valor para poder crearlo.
Nota: todos los albaranes generados son contabilizados al momento de su generación, esto es debido al proceso de Inventario permanente, el cual registra contablemente la minoración de coste de stock y suma un adeudo del coste en las facturas por cobrar.
Factura de Venta
Las facturas generadas desde el circuito de ventas, tendrán ya toda la información requerida sobre la gestión de la doble unidad.

En los procesos de la Gestión de Stocks
La gestión de la doble unidad está presente en los siguientes procedimientos, en todos ellos se solicitará el registro de la doble unidad:
Inventarios: Al realizar nuestros inventarios, tendremos que indicar el valor de la doble unidad.
Actualizaciones de Stock: la actualización del stock se realiza de la misma forma que anteriormente, en este caso todos los procesos de actualización desde los circuitos de ventas y compras ya vendrán con estos datos proporcionados, ya que son necesarios para su registro, tal y como lo hemos visto anteriormente.
Movimientos Manuales: todo movimiento manual que se realice, requerirá del dato de la segunda unidad de medida.
Ajustes de Stock: para realizar cualquier ajuste deberá tener en cuenta ambas unidades.
En la Valoración Actual de almacenes, se realiza en base a la unidad de medida uno (Stock Físico), pero tiene en cuenta el valor del stock en la segunda unidad (Stock Físico 2)

Gestión de Inventarios Permanente
La gestión de Inventarios permanente, permite un control constante de los inventaros, al llevar el registro de cada unidad que entra y sale del almacén.
Para poder llevar un inventario permanente es necesario realizar asientos contables con cada movimiento de almacén.
Configuración
En la pantalla de parámetros de la aplicación, deberemos activar el parámetro CONT_MOV indicando el valor “1 | Sí”, con esto indicaremos que vamos a trabajar con el inventario permanente.
Si este parámetro se encuentra desactivado (CONT_MOV = “0 | No”) la aplicación funcionará con la gestión de Inventario Periódico que es el estándar actual.
Para artículos con gestión de Stocks deberemos establecer la cuenta contable “CC. Stocks” (Mantenimiento de Artículos > General > Cuentas Contables). O en su defecto C.C. Stocks en el mantenimiento de familias de artículos (Tipo de Artículo > Familia > ).
De cara a realizar el asiento de contabilización de los albaranes de compra y venta deberá asociar a las fichas de proveedor y cliente respectivamente, las cuentas contables para:
Factura pendiente por recibir (CC. Fra. Pdte.): 4009: Proveedores Facturas Pendientes por Recibir.
Factura pendiente (CC. Fra. Pdte.), 4309: Clientes, facturas pendientes de formalizar.
De cara a contabilizar los movimientos manuales de Stock, en el mantenimiento de Tipos de Movimiento deberemos indicar los tipos de movimientos que generarán un apunte contable, para ello:
Activamos la marca “R Contabilizar”.
Si contabilizar = FALSE: Igual que hasta ahora.
Al activar esta marca se activan los siguientes campos, en los que indicaremos la información correspondiente:
C. Contable.
Icono de Desglose Analítico: podrá introducir información si la cuenta contable está marcada como analítica.

Contabilizar Albaranes de Compra
El proceso de Contabilización de Albaran de Compra nos permitirá generar los asientos contables de entrada de material. La contabilización se genera automáticamente al actualizar el stock.
Nota: recuerde que al generar un Albarán de Compra se realiza la actualización de stock, este proceso puede ser automático o bien manual dependiendo de su configuración.
Debe tener en cuenta los siguientes aspectos:
Para que los artículos puedan ser contabilizados deben cumplir con los siguientes requisitos:
Debe haberse actualizado el stock.
Existe una serie de restricciones a la actualización por las cuales puede que aunque se ejecute la actualización de stocks, una o más líneas no se hayan actualizado.
No debe tener asociada una factura contabilizada.
El asiento que se genera en la contabilización es el siguiente:
Podremos diferenciar las líneas de albarán que han sido contabilizadas ya que se muestran en negrita.
Si se ha realizado el proceso de contabilización automático y alguna línea se quedara sin contabilizar (no cumple alguno de los requisitos del punto 1), una vez haya identificado el problema, deberá lanzar la contabilización.
Para lanzar la contabilización, ejecute el proceso “Contabilizar Líneas de Albarán” ya sea desde el botón de procesos (para todas las líneas) o bien desde el menú contextual para la línea que quiera contabilizar.
Se muestra la pantalla de simulación contable con la información del asiento que se va a generar.
Si desea modificar el asiento ya realizado, deberá eliminarlo primero mediante el proceso de descontabilización, como se muestra en el siguiente apartado. Una vez eliminado vuelva a lanzar la contabilización como se indica en el punto 5.
Descontabilizar Albarán de Compra
Proceso:
Para realizar la descontabilización, deberá seleccionar el proceso “Descontabilizar Líneas Albarán”.
Se muestran los datos de la contabilización, pulse “Aceptar”.
Contabilización / Descontabilización masiva de Albaranes de Compra
Mediante la pantalla “Contabilización Masiva de Albaranes de Compra” podrá ejecutar el proceso correspondiente para contabilizar y descontabilizar las líneas seleccionadas de los albaranes.
Modificación de la contabilización de Facturas de Compra
El asiento de la factura de compra, para líneas cuyo albarán ha sido contabilizado, debe ser el siguiente:
Analítica
El albarán de compra no intervienen cuentas de analítica. Factura de compra:
Si el albarán de compra está contabilizado, no hay cuentas de analítica.
Si el albarán de compra no está contabilizado o no tiene albarán de compra la analítica tendrá funcionamiento estándar.

Contabilizar Albaranes de Ventas
El proceso de Contabilización de Albaran de Venta se genera automáticamente al actualizarse el stock.
Nota: recuerde que al generar un Albarán de Venta se genera la actualización de stock que indica la salida del nuevo material, este proceso puede ser automático o bien manual dependiendo de su configuración.
Debe tener en cuenta los siguientes aspectos:
Para que los artículos puedan ser contabilizados deben cumplir con los siguientes requisitos:
Debe haberse actualizado el stock.
Existe una serie de restricciones a la actualización por las cuales puede que aunque se ejecute la actualización de stocks, una o más líneas no se hayan actualizado.
No debe tener asociada una factura contabilizada.
El asiento que se genera en la contabilización es el siguiente:
Podremos diferenciar las líneas de albarán que han sido contabilizadas ya que se muestran en negrita.
Si se ha realizado el proceso de contabilización automático y alguna línea se quedara sin contabilizar (no cumple alguno de los requisitos del punto 1), una vez haya identificado el problema, deberá lanzar la contabilización.
Para lanzar la contabilización, ejecute el proceso “Contabilizar Líneas de Albarán” ya sea desde el botón de procesos (para todas las líneas) o bien desde el menú contextual para la línea que quiera contabilizar.
Se muestra la pantalla de simulación contable con la información del asiento que se va a generar.
Si desea modificar el asiento ya realizado, deberá eliminarlo primero mediante el proceso de descontabilización, como se muestra en el siguiente apartado. Una vez eliminado vuelva a lanzar la contabilización como se indica en el punto 5.
Descontabilizar Albarán de Venta
Este proceso elimina el asiento contable (si se ha generado la correspondiente factura no se puede eliminar el asiento). Esta acción se puede lanzar desde el listado de acciones del Albarán de Venta o sobre la propia línea del albarán a través del menú contextual.
Para realizar la descontabilización, deberá seleccionar el proceso “Descontabilizar Líneas Albarán”.
Se muestran los datos de la contabilización, pulse “Aceptar”.
Contabilización / Descontabilización Masiva de Albaranes de Venta
Mediante la pantalla “Contabilización Masiva de Albaranes de Venta” podrá ejecutar el proceso correspondiente para contabilizar y descontabilizar las líneas seleccionadas de los albaranes.
Modificación de la contabilización de Facturas de Venta
El asiento de la factura de venta, para líneas cuyo albarán ha sido contabilizado, debe ser el siguiente:
Analítica
El Albarán de venta no intervienen cuentas de analítica.
La factura de venta:
Si el albarán de venta no está contabilizado o la factura no tiene albarán de venta asociado: funcionamiento estándar de analítica.
Si el albarán de venta está contabilizado: la imputación analítica del costo de la venta será la asociada a la línea de venta correspondiente

Contabilizar Movimientos Manuales de Stock
Para contabilizar los movimientos manuales de Stock:
Una vez generado el movimiento, se valida el registro y se volcarán los datos referentes a la gestión de Inventario Permanente:
CC. Stock: la cuenta asociada al artículo.
C. Contable asociado al tipo de movimiento (mantenimiento de tipos de movimiento).
Analítica: vinculada al tipo de movimiento (modificable).
Ejecutamos el proceso asociado “Contabilizar Movimientos”.
Se muestra la pantalla de contabilización donde se mostraran los asientos que se van a realizar
El movimiento queda en estado “Contabilizado” (Campo contabilizado).
La analítica a imputar será la establecida en la pantalla Movimientos Manuales.
Descontabilizar Movimientos Manuales de Stock
Para descontabilizar el movimiento manual, únicamente seleccione el proceso asociado “Descontabilizar Movimientos”.
Contabilización/ Descontabilización Masiva de Movimientos de Stock
Mediante la pantalla “Contabilización de Movimientos de Stock” podrá ejecutar el proceso correspondiente para contabilizar y descontabilizar las líneas seleccionadas de los albaranes.

Contabilizar la Imputación de Gastos especiales
Este proceso desencadena una modificación de la valoración del stock por lo que debe generar el correspondiente asiento:
Para descontabilizar una imputación de gasto, ejecute el proceso “Descontabilizar Líneas de Albarán”.

Contabilizar los Ajustes de Inventarios
La realización de inventarios físicos da lugar a diferencias entre el stock registrado en la aplicación y el stock real. Esta diferencia se debe ajustar mediante los correspondientes movimientos contables y de stock. Desde el punto de vista contable esto implica realizar un ajuste en positivo o negativo:
En el Mantenimiento de Tipos de Movimiento para el tipo Inventario se deben poder indicar 2 cuentas contables:
Cuenta de ingresos. Se utilizará cuando Stock Real > Stock Teórico
Cuenta de gastos. Se utilizará cuando Stock Real < Stock Teórico
Si el inventario real es > inventario teórico hay que hacer un asiento de ajuste negativo:
La analítica a imputar será la establecida en la pantalla Movimientos Manuales.

Gestión de Kits de artículos
Un artículo de Tipo Kit es un producto comercial que agrupa un conjunto de artículos que se tratan como un único elemento en el proceso de venta o compra. Al realizar las compras o las ventas, el proceso se lanza contra el artículo kit, sin embargo, cuando registramos los ingresos o salidas de almacén, imputamos la cantidad de producto de sus componentes.
El esquema de información de un producto de tipo kit es el siguiente:
Referencia comercial = Tipo: ☑ Kit + ☑ Venta + ☑ Compra
Precio: se establece para el artículo de tipo kit.
Stock: no se gestiona para la referencia de tipo Kit. En los procesos de actualización de stock, se descuentan los artículos que componen la estructura del producto comercial.
Estructura: listado de artículos, y cantidades, que conforman la referencia de tipo kit.

Consulta de Disponibilidad
Permite conocer además del stock disponible (teórico) por Artículo y Almacén el conjunto de información que corresponda a todo lo que represente un aumento o merma en dicha cantidad: el producto que está pendiende de entrada o salida de stock, etc.
Los datos de la consulta son los siguientes:
Artículo y Almacén en que se encuentra.
Stock físico de un artículo en el almacén dado en la misma línea.
Cantidad Pedida (ENT): Se muestra la cantidad de artículo está pendiente de ser recibida en nuestros almacenes ya sea por compras (pedidos de compra pendientes de servir), o por órdenes de fabricación terminadas (artículos en proceso de producción).
Pendiente (SAL): Se muestra la cantidad de artículo pendiente de ser expedida de nuestro almacén ya sea por ventas (pedidos de venta pendientes de servir) o bien por órdenes de fabricación (consumibles que no han sido aún descontados de stock).
Disponible: muestra el total disponible teniendo en cuenta el stock físico, las entradas y las salidas: Stock + Cantidad Pedida (ENT) – Pendiente (SAL).
 Acceso al detalle de la Disponibilidad de Artículos en la que se muestra información de los procesos implicados.
Información de Disponibilidad
Stock Actual: información sobre el stock existente en cada uno de los almacenes asociados al artículo.
Pedidos Pendientes de Servir: informa detalladamente de cada uno de los pedidos pendientes de servir existentes contra el artículo activo.
Se puede realizar la consulta bien por el código de cliente, bien por el código que el cliente asocia al  pedido.
El proceso se realiza teniendo en cuenta la fecha establecida en cabecera, entendiendo este dato como ‘tope’ para el cálculo.
Se procesarán todos aquellos pedidos cuya Fecha de Pedido sea inferior a la fecha establecida en la cabecera de la pantalla.
Cómo repercute en el resto: ordenes de fabricación (Fecha Inicio), pedidos materia prima (fecha pedido), etc.
Ordenes de Fabricación en Curso: se informa del número de orden de fabricación en curso asociada al artículo, así como de su fecha de inicio y Fin, de su situación y de la cantidad de unidades que intervienen en dicha orden de fabricación.
Se puede realizar la consulta según la situaciónde la orden de fabricación, esto es, Planificada, Iniciada, etc.
Albaranes Pendientes de Actualizar: relación de los albaranes pendientes de actualizar junto con el detalle de cada uno de ellos.
Permite realizar la consulta bien por el código identificador del cliente, o bien por la fecha del albarán.
Evolución Disponibilidad: se muestran los movimientos de stock en orden cronológico para el artículo activo.
Se muestra el tipo de documentoasociado al movimiento, junto a su código identificador, la situación, la fecha y la cantidad del artículo en él recogida;  además de estos datos el sistema indica el total del stock disponible como resultado de cada uno de los movimientos.
Disponibilidad de Material Kit: si el artículo es de tipo Kit, se informa de sus componentes (artículos), el almacén en que se encuentran localizados y su stock.
Disponibilidad de Materia Prima: informa los plazos de disponibilidad de los componentes del artículo, en el caso de que éste tenga una estructura asociada.
El sistema muestra tanto el código de artículo,  como su descripción, el almacén asociado al componente, el stock disponible, la necesidad de fabricación del componente,  el disponible (diferencia entre el stock y la necesidad del mismo) y la cantidades pendientes de recibir en el supuesto de que estos componentes sean subcontratados a un ente externo.
Puede realizar la consulta según el código del artículo (componente), el almacén de éste y la situación de la orden de fabricación.
Pedidos Compra Materia Prima: informa detalladamente los datosde cada uno de los pedidos asociados a cada uno de los componentes del artículo.
Es posible realizar la consulta bien por el código de artículo (componente), bien por el código del almacén asociado a cada uno de los componentes.
Disponibilidad de Números de Serie: informa de los números de serie asociados al artículo activo.
Disponibilidad de Lote: informa de la relación de Lotes-Ubicación asociados al artículo activo, junto a las cantidades de cada uno de estos y su fecha de caducidad.

Consulta de Stock de Seguridad
Pantalla de tipo consulta interactiva en la que se muestra la diferencia entre el stock físico y el stock de seguridad (stock Físico – Stock Seguridad), esto le facilita saber cuándo tiene que realizar el reaprovisionamiento utilizando únicamente este concepto.

Consulta de Doble Unidad
Permite consultar el stock físico en la unidad de almacenamiento (ud. interna) y en otra unidad de medida utilizada en la operativa de Ventas, Compras o Fabricación.
Recuerda que debe haber un Factor de Conversión entre estas unidades de medida, a través de las Conversiones Genéricas o en la propia información del artículo (apartado Unidades).

Consultas de Lotes
Permite consultar de forma centralizada la información de los artículos gestionados por Lotes – Ubicación. También permite bloquear Lotes para impedir las expediciones de mercancía.
Para ello seleccionará la columna ‘Bloqueado’ y el sistema insertará el icono  como identificador del bloqueo.
Informes:
Diferencias de Stock: muestra la información del stock de cada lote indicando la diferencia con el stock total del artículo.
Listado de Artículos por Lotes: muestra la información del stock de cada lote de artículo.

Consulta Fecha Lote
Esta pantalla le permitirá consultar el stock existente por lote de artículo en los diferentes almacenes / ubicación (si las gestiona).

Consulta de Números de Serie
Además de en la pantalla de Disponibilidad de Artículos, solapa Números de Serie, puede acceder a esta pantalla de tipo consulta interactiva para obtener información de forma agrupada de todas sus referencias.

Información Cliente
El maestro de Clientes es uno de los maestros de información principales de Solmicro ERP. En este registraremos y/o consultaremos la información de cada uno de nuestros Clientes.
Cada apartado de información permitirá gestionar las operaciones asociadas a cada Cliente en cada uno de los procesos de Solmicro ERP por lo que es necesario mantener un correcto registro de la información.
A continuación detallamos la información de cada uno de los apartados así como las operaciones y/o procesos con los que están asociados.
A continuación indicamos la información que participa en el registro de los Clientes.
Parámetros funcionales asociados al registro de Clientes.
Mantenimientos Auxiliares




"""
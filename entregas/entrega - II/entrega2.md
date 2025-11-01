
# Implementación Pipeline de Integración Continua

## Caso Pipeline Exitoso

En este caso ejecutaremos la construcción de la aplicación blacklist en un entorno de Elastic Beanstalk a través de un pipeline configurado en Amazon Codepipeline. 

La idea del ejercicio es que durante la construcción inicial de la aplicación así como despues de ejecutar un commit, las pruebas se ejecuten automáticamente, los test pasen y la aplicación se construya correctamente. 

Esperamos que al finalizar la construcción se genere un artefacto (en el bucket de s3) con la aplicación construida a partir del repositorio fuente.

### Preparación del ejercicio

Para ejecutar este ejercicio contamos con: 

Un fork del repositorio original de la aplicación *BlacList* en la cuenta de github desde la cual se van a realizar las pruebas. Esto nos facilita la conexión pues genera una copia de la aplicación desde la cual tenemos un rol de propietario.

![fork](pipeline_IC_exitoso/fork_previo.png)

Una conexion con el repositorio de github desde el cual se van a realizar las pruebas. Configurada desde Amazon Codepipeline

![conexion](pipeline_IC_exitoso/Conexion_previo.png)

### Ejecucion del ejercicio

Para iniciar con el ejercicio vamos a Amazon Codepipeline, seleccionamos la opción **crear canalización** e iniciamos con la configuración.

Llamamos nuestra canalización *BlackList_Pipeline*

![configuracion](pipeline_IC_exitoso/configuracion.png)

El paso a seguir es la definición del origen del pipeline para lo cual utilizamos el proveedor GitHub (a través de Github app), la [conexión](#preparación-del-ejercicio) previamente configurada y el repositorio habilitado mediante la conexión. 

![origen](pipeline_IC_exitoso/etapa_origen.png)

Posteriormente, en el mismo proceso de creación de la canalización, creamos un proyecto de compliación de amazon Codebuild llamado *Blaclists_compilacion_proyecto* 

![creacion proyecto 1](pipeline_IC_exitoso/creacion_proyecto.png)

En el proyecto de compilación  utilizamos un archivo de especificación de compilación (que ya está creado en el proyecto de Github) el cual se llama buildspect.yml. Ingresamos la ruta relativa del archivo de especificación.

![creacion proyecto 2](pipeline_IC_exitoso/creacion_proyecto_II.png)

Una vez creado el proyecto, se termina de configurar la compilación con el proyecto creado.

![compilacion](pipeline_IC_exitoso/compilacion.png)

Para este ejercicio se omitieron las etapas de pruebas y de despliegue. 

Una vez finalizada la configuración, se lanzó la construcción del Pipeline.

Podemos validar que tanto la habilitación de los recursos como la construcción de la aplicación fueron exitosos.

Nótese que la fuente del recurso es "build pipeline" que es el nombre del commit del repositorio con el que se hizo la construcción inicial.

![build](pipeline_IC_exitoso/build.png)

Podemos validar que en la etapa de construcción las pruebas se ejecutaron de forma exitosa.

![pruebas build](pipeline_IC_exitoso/pruebas_build.png)

El siguiente paso es hacer un commit en el repositorio fuente. El commit se llamó "commit 1 pipeline" para probar ahora que la ejecución del push a la rama main del repositorio fuente desencadene una nueva ejecución del proceso de construcción. 

Podemos validar que una vez hecho el nuevo commit, el pipeline inicia una nueva ejecución encima de la ejecución de la construccion inicial (build pipeline), ahora con el nombre del commit

![commit](pipeline_IC_exitoso/coomit_1.PNG)

Una vez finalizada, validamos que la segunda ejecución (la del commit 1) también fue exitosa

![despliegue commit](pipeline_IC_exitoso/despliegue_commit.png)

![ejecuciones](pipeline_IC_exitoso/ejecuciones.png)

Validamos también que se ejecutaron las pruebas nuevamente

![pruebas commit](pipeline_IC_exitoso/pruebas_commit.png)

podemos confirmar en S3 que se generaron 2 artefactos, uno para la ejecución inicial y uno para el commit realizado

![artefactos](pipeline_IC_exitoso/artefactos.png)

Al descargar el artefacto, podemos confirmar que este contiene la aplicación construida.

![zip artefacto](pipeline_IC_exitoso/zip_artefacto.png)

Con esto concluye el ejercicio exitoso de integración continua.

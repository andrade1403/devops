# Documento de entrega I

## Punto 1a
Para la configuración de Amazon RDS dentro del servicio AWS Elastic Beanstalk, durante el proceso de creación del entorno se habilitó la opción correspondiente a RDS, tal como se muestra en la siguiente imagen:

![rds](rds.png)

En dicha configuración, se especificó una base de datos con motor PostgreSQL y cuando el servicio de AWS Elastic Beanstalk eliminé la aplicación, la base de datos también será eliminada ya que estamos en un entorno de desarrollo y no requerimos guardar instancias de AWS RDS.

Para permitir que la aplicación utilice esta base de datos, dentro del archivo principal de la aplicación `application.py` se definió la conexión mediante variables de entorno, las cuales son generadas automáticamente por Beanstalk al momento de crear el entorno con la instancia de RDS asociada.

En el siguiente fragmento de código se muestra la configuración utilizada para establecer la conexión con la base de datos:

```python
#Creamos la aplicacion de Flask
application = Flask(__name__)

#Ponemos configuraciones de la app
application.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('RDS_USERNAME')}:{os.getenv('RDS_PASSWORD')}"
    f"@{os.getenv('RDS_HOSTNAME')}:{os.getenv('RDS_PORT')}/{os.getenv('RDS_DB_NAME')}"
)
```

## Punto 1c

Para la configuración de los health checks en AWS Elastic Beanstalk, se define un parámetro dentro del archivo de configuración del entorno `.ebextensions`. En este archivo, se especifica el endpoint de verificación de estado mediante la siguiente instrucción:

```
option_settings:
  aws:elasticbeanstalk:application:
    Application Healthcheck URL: /v1/blacklists/health

  aws:elasticbeanstalk:environment:process:default:
    HealthCheckPath: /v1/blacklists/health
    HealthCheckInterval: 10
    HealthCheckTimeout: 5
    HealthyThresholdCount: 3
    UnhealthyThresholdCount: 5
```

Dentro de la aplicación desarrollada con Flask, se implementa un endpoint `/v1/blacklists/health` que responde con un código HTTP 200, indicando que la aplicación se encuentra desplegada y funcionando correctamente.

A través del archivo `.ebextensions`, se establece la ruta de este endpoint, así como los parámetros asociados a los ciclos de verificación, que incluyen la frecuencia de los chequeos y la tolerancia a errores definida por Elastic Beanstalk para determinar el estado de salud del entorno.
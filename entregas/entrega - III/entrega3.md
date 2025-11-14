## Pipeline de Integración Continua exitoso y de entrega continua fallido

Para provocar que la ejecución del pipeline tenga una integración continua exitosa pero una entrega continua fallida, se modificará el archivo `buildspec.yml`, específicamente en la sección correspondiente a los artefactos. Actualmente, el archivo está definido de la siguiente manera:

```
artifacts:
  base-directory: blacklist_app
  files:
    - '**/*'
    - imagedefinitions.json
    - imageDetail.json
  secondary-artifacts:
    DefinitionArtifact:
      files:
        - appspec.yaml
        - taskdef.json
    ImageArtifact:
      files:
        - imageDetail.json
```

La línea `base-directory: blacklist_app` indica que los artefactos deben empaquetarse a partir de ese directorio y luego ser almacenados en el bucket s3 generado por defecto. La modificación consiste en eliminar dicha declaración de `base-directory`, de modo que el empaquetado de los artefactos se realice desde la raíz del repositorio. Como resultado, los archivos `taskdef.json` y `appspec.json`, que contienen la definición del task de ECS y del servicio de ECS a crear, no estarán disponibles para CodeDeploy. Esto provocará que la fase de despliegue falle dentro del pipeline.

## Links de referencia
- Video: https://uniandes-my.sharepoint.com/:v:/g/personal/d_andrades_uniandes_edu_co/IQBlmYsNVJ2ET4UO-x876HC_AeFuXthqIUK6OkAAU8c28p4
- Repositorio: https://github.com/andrade1403/devops.git
- Colección POSTMAN: https://documenter.getpostman.com/view/49127146/2sB3QMLpC6

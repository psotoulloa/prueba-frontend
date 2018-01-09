## Como insertar una tarea 

```javascript
var task = Tasks.save({
		"autor": "Patricio",  
		"descripcion": "Hola mundo 1",
		"estado": "pendiente",
		"fecha_comprometida": "2017-05-29"
	}).$promise.then(function(){
		console.log(task)
	});
```

## Como buscar las tareas pendientes de un usuario

```javascript
var tareasPendientes = Tasks.query({'q':JSON.stringify({"filters":[{"and": [
		{"name": "autor", "op": "eq", "val": "Patricio"}]},
		{"name": "estado", "op": "eq", "val": "pendiente"}
	]})});
```

## Como modificar una tarea 
```javascript
var tarea = {
	"autor": "Patricio",  
	"descripcion": "Hola mundo 1",
	"estado": "realizada",
	"fecha_comprometida": "2017-05-29",
	"id" : 1
}
Tasks.update( { "id" : tarea.id } ,tarea);
```

## Como elimiar una tarea
```javascript
Tasks.remove( { "id" : tarea.id } );
```

## Paginación
Para paginar deberás agregar el parámetro "page" a la ejecución del método query mayor información en ngResource
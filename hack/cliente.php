<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Registrar</title>
</head>

<body>
<?php
	include("conexion.php");
		
	$nombre= $_POST["nombre"];
	$usuario = $_POST["usuario"];
	$contrasenaac= $_POST['contraac'];
	
	
	$insertar = "INSERT into clientes VALUES ('$nombre', '$usuario', '$contrasenaac')";

	$tabla="CREATE table $usuario(id INT(50), foto VARCHAR(300), producto VARCHAR(100), marca VARCHAR(100), precio FLOAT(20))";
	

	$resultado = mysqli_query($conexion, $insertar)
		or die (header("Location: index.html"));
	$create = mysqli_query($conexion, $tabla)or die (header("Location: index.html"));


		
	mysqli_close($conexion);
	include("procesoclientes.php");	
	?>
    <a href="index.html" target="_self">Regresar</a>
</body>
</html>
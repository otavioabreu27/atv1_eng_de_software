CREATE TABLE usuario(
	id_usuario int auto_increment,
	nome char(30) not null,
	email char(40) not null,
	senha char(20) not null,
	PRIMARY KEY(id_usuario)
);

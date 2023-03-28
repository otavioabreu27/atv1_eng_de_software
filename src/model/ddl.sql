CREATE DATABASE cadastro;

CREATE TABLE usuario(
	id_usuario int auto_increment primary key,
	nome char(30) not null,
	email char(40) not null,
	senha char(20) not null,
);
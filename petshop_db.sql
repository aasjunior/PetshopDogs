create database PetShop
use PetShop

create table Funcionarios(
	id int(11) auto_increment,
    nome varchar(250) not null,
    email varchar(250) not null,
    telefone varchar(15) not null,
    senha varchar(250) not null,
    imagem longblob,
    primary key(id)
)

select * from Funcionarios
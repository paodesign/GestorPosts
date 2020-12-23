create database Viajes 
use Viajes

create table posts(
id int IDENTITY(1,1) not null,
titulo varchar(100) not null,
fecha datetime2,
descripcion nvarchar(MAX),
autor_dni int not null,
constraint pk_post primary key(id),
constraint fk_post_autor foreign key(autor_dni) references autores(dni)
)

create table autores(
dni int not null,
nombre varchar(70) not null,
fecha_nac datetime2
constraint pk_autor primary key(dni)
)

INSERT INTO [dbo].[posts]
           ([titulo]
           ,[fecha]
           ,[descripcion]
           ,[autor_dni])
     VALUES
           ('sapo de otro poso',
          GETDATE(),
           'cuento',
           23456890)
GO

INSERT INTO [dbo].[autores]
           ([dni]
           ,[nombre]
           ,[fecha_nac])
     VALUES
           (34845678,
           'Adam',
           '01-07-80')
GO

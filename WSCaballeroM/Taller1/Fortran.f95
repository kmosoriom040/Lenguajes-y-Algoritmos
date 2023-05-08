Fortran
program hola_mundo
implicit none
integer :: i, x

i = 1

write(,) "Numero de veces que desea repetir Hola mundo:"
read(,) x

do while (i <= x)
write(,) "Hola mundo"
i = i + 1
end do

end program hola_mundo
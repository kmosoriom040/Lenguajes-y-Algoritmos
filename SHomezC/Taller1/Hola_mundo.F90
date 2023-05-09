program hola_mundo
    implicit none
    integer :: n, i
    write(*,*) 'Ingrese la cantidad de veces que desea imprimir ''Hola Mundo'': '
    read(*,*) n
    do i = 1, n
        write(*,*) 'Hola Mundo'
    end do
end program hola_mundo

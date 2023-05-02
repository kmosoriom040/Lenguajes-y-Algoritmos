program Hola_mundo
    implicit none
    integer :: n, i
    write(*,*) "Ingrese la cantidad de veces que desea sea impresa la frase 'Hola mundo' "
    read(*,*) n
    do i = 1, n
        write(*,'(a)') "Hola mundo "
    end do
end program Hola_mundo

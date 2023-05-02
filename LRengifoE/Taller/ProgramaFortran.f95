program Hola_mundo
    implicit none
    integer :: n, i
    write(*,*) "Bienvenido. Ingrese el valor que desea visualizar 'Hola mundo' en su pantalla "
    read(*,*) n
    do i = 1, n
        write(*,'(a)') "Hola mundo "
    end do
end program Hola_mundo

program Holas_Mundo
    implicit none
    integer :: n, i
    write(*,*) "Escriba el numero de 'Hola Mundo!' que desee ver en pantalla en forma de valor numerico: "
    read(*,*) n
    do i = 1, n
        write(*,'(a)') "Hola mundo "
    end do
end program Holas_Mundo

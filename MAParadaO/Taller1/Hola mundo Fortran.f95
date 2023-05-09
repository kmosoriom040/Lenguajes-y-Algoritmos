program holamundo
    implicit none
    integer :: n, i
    write(*,*) "Ingrese una variable:"
    read(*,*) n
    do i = 1, n
        write(*,'(a)') "hola mundo "
    end do
end program holamundo

program hola_mundo
  implicit none
  integer :: n, i

  write(*,*) 'Ingresa el número de veces que quieres imprimir "hola mundo": '
  read(*,*) n

  do i = 1, n
    write(*,*) 'hola mundo'
  end do

end program hola_mundo

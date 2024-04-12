  
def crearsublistas():
    num_sublistas = int(input("Ingrese la cantidad de sublistas que desea crear: "))
    main_list = []
    for i in range(num_sublistas):
        sublista = []
        while True:
            num = int(input("Ingrese un número para la sublistas (ingrese -1 para terminar): "))
            if num == -1:
                break
            sublista.append(num)
        main_list.append(sublista)
    return main_list

###  ##   ## ##             ## ##   ### ###            ### ##   ### ##   ## ##    ### ###  ### ###  
# ## ##  ##   ##           ##   ##   ##  ##            ##  ##   ##  ##  ##   ##   ##  ##   ##  ##  
## # #  ##   ##           ####      ##                 ##  ##   ##  ##  ##   ##   ##       ##      
##  ##   ##   ##            #####    ## ##             ##  ##   ## ##   ##   ##   ## ##    ## ##   
##   ##  ##   ##               ###   ##                ## ##    ## ##   ##   ##   ##       ##      
##   ##  ##   ##           ##   ##   ##  ##            ##       ##  ##  ##   ##   ##       ##  ##  
##   ##   ## ##             ## ##   ### ###           ####     #### ##   ## ##   ####      ### ###  
                                                                                            



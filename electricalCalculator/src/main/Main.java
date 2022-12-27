package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.Arrays;

import pearls.Help;

public class Main {

	public static void main(String[] args) {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Hello! Welcome to this shitty program!\nDo you need some help?\nYou have these options:\n");
		
		System.out.println(Arrays.toString(scanDir()));
		
		
//	    inp1 = 0
//	    while inp1 <= 0:
//	        try:
//	            inp1 = int(input('\nYour choice: '))
//	            lenop = len(pyfiles)
//	            if inp1 > lenop:
//	                print('I\'m sorry, that option isn\'t ready yet')
//	                timer_5s()
//
//	        except:
//	            print('Sorry, what you said?')
//	            inp1 = 0

	}
	
	public static String[] scanDir() {
		String sCarpAct = System.getProperty(Main.class.getResourceAsStream("/pearls"));
		File carpeta = new File(sCarpAct);
		
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
		    System.out.println("No hay elementos dentro de la carpeta actual");
		    return null;
		}
		else {
		    for (int i=0; i< listado.length; i++) {
		        System.out.println(listado[i]);
		    }
		}
		
		return listado;
	}

}

package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
//		System.out.println("Hello! Welcome to this shitty program!\nDo you need some help?\nYou have these options:\n");

		String[] pearls = scanDir();

		for (int i = 0; i < pearls.length; i++)
			System.out.println((i + 1) + ": " + pearls[i]);

		int optionSelected = 0;

		System.out.print("\nChoose an option: ");

		while ((optionSelected = Integer.parseInt(in.readLine())) > pearls.length || optionSelected == 0) {
			if (optionSelected > pearls.length || optionSelected == 0)
				System.out.print("\nWe didn't implemented that option yet, sorry. :(\nTry again: ");
		}
		
		clearConsole();

		System.out.println("Your selection: " + optionSelected);
		System.out.println("\nLaunching " + pearls[optionSelected - 1] + "...");

	}

	public static String[] scanDir() {
		File carpeta = new File("resources/pearls");
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
			System.out.println("No hay elementos dentro de la carpeta actual");
			return null;
		}
		return listado;
	}

	public static void clearConsole() {
		//Clears Screen in java
	    try {
	        if (System.getProperty("os.name").contains("Windows"))
	        	new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
	        else
	            Runtime.getRuntime().exec("clear");
	    } catch (IOException | InterruptedException ex) {}
	}

}

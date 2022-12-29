package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.ProcessBuilder.Redirect;

public class Main {

	public static void main(String[] args) throws IOException {
		clearConsole();
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Hello! Welcome to this shitty program!\nDo you need some help?\nYou have these options:\n");
		String[] scripts = scanDir();

		for (int i = 0; i < scripts.length; i++)
			System.out.println((i + 1) + ": " + scripts[i]);

		int optionSelected = 0;

		System.out.print("\nChoose an option: ");

		while ((optionSelected = Integer.parseInt(in.readLine())) > scripts.length || optionSelected == 0) {
			if (optionSelected > scripts.length || optionSelected == 0)
				System.out.print("\nWe didn't implemented that option yet, sorry. :(\nTry again: ");
		}

		clearConsole();

		System.out.println("Your selection: " + optionSelected);

		openFile(scripts[optionSelected - 1], in);

	}

	public static void openFile(String file, BufferedReader in) throws IOException {
		clearConsole();
		System.out.print("\nLaunching " + file);
		
		laTonteriaDeLosPuntitos(".", 3);
		clearConsole();
		
		String x = "y";
		while (x.toLowerCase() == "y") {
			String[] cmd = {"java", "-cp", getResPath(), "scripts." + file.replaceAll(".class", "")};
			Process p = new ProcessBuilder(cmd).redirectError(Redirect.INHERIT) // No se muy bien lo que hace, lo saqué de internet
			                                   .redirectOutput(Redirect.INHERIT) // pero con esto se puede abrir una clase usando la terminal
			                                   .start();
			System.out.println();
			try {
				p.waitFor();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.print("\nDo you want to continue using this script? (y/N): ");
			x = in.readLine();
			
			if (x.toLowerCase() == "y") { // Not working the moment
				clearConsole();
				System.out.println("Reloading" + file + "...\n");
			}
		}
		System.out.println("Exiting the script.");
	}

	public static String getResPath() {
		File f = new File("");
		return f.getAbsolutePath();
	}

	public static String[] scanDir() {
		File carpeta = new File("scripts");
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
			System.out.println("No hay elementos dentro de la carpeta actual");
			return null;
		}
		return listado;
	}
	
	public static void laTonteriaDeLosPuntitos(String msj, int duration) {
		for(int i = 0; i < 3; i++) {
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.print(".");
		}
		// Pequeño método que en una línea repite el caracter o cadena que queramos y el número de veces
		// No cumple ninguna función, pero en Python lo había hecho así y me salió de ahí meterlo aquí
	}

	public static void clearConsole() {
		// Clears Screen in java
		String[] cmd = {"clear"};
		try {
			if (System.getProperty("os.name").contains("Windows"))
				new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
			else
				Runtime.getRuntime().exec(cmd);
		} catch (IOException | InterruptedException ex) {
		}
	}

}

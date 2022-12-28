package main;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.ProcessBuilder.Redirect;

public class Main {

	public static void main(String[] args) throws IOException {
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
		System.out.println("\nLaunching " + scripts[optionSelected - 1] + "...");

		openFile(scripts[optionSelected - 1], in);

	}

	public static void openFile(String file, BufferedReader in) throws IOException {
		clearConsole();
		System.out.println("\nLaunching " + file + "...");
		String x = "y";
		while (x.toLowerCase() == "y") {
//			System.out.println("java " + getResPath() + "\\scripts." + file.replaceAll(".class", ""));
//			Runtime.getRuntime().exec("java " + getResPath() + "\\scripts." + file.replaceAll(".class", ""));
			String[] cmd = {"java", "-cp", getResPath() + "\\scripts.", file.replaceAll(".class", "")};
			Process p = new ProcessBuilder(cmd).redirectError(Redirect.INHERIT)
			                                   .redirectOutput(Redirect.INHERIT)
			                                   .start();
			try {
				p.waitFor();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println("\nDo you want to continue using this script? (y/N)");
			x = in.readLine();
			
			if (x.toLowerCase() == "y") {
				clearConsole();
				System.out.println("Reloading" + file + "...\n");
			}
		}
		System.out.println("Exiting the script.");
	}

	public static String getResPath() {
		File f = new File("resources/");
		return f.getAbsolutePath();
	}

	public static String[] scanDir() {
		File carpeta = new File("resources/scripts");
		String[] listado = carpeta.list();
		if (listado == null || listado.length == 0) {
			System.out.println("No hay elementos dentro de la carpeta actual");
			return null;
		}
		return listado;
	}

	public static void clearConsole() {
		// Clears Screen in java
		try {
			if (System.getProperty("os.name").contains("Windows"))
				new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
			else
				Runtime.getRuntime().exec("clear");
		} catch (IOException | InterruptedException ex) {
		}
	}

}

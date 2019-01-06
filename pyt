package pyteshestvie;
import java.util.Scanner;
import java.text.DecimalFormat;
public class pyteshestvie {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Scanner reader = new Scanner (System.in);
		DecimalFormat df = new DecimalFormat("##.##");
		
		double budget = scanner.nextDouble();
		String season = reader.next();
		String destination;
		String type;
		double spend;
		double percent;
		
		if(budget < 10 || budget > 5000) {
			System.out.println
			("The budget cannot be under 10 or above 5000!");
			scanner.close();
			return;
		}
		else if (!season.equals("summer") && !season.equals("winter")) {
			System.out.println
			("The season cannot be different from summer or winter!");
			scanner.close();
			return;
		}
		
		if(budget <= 100) {
			destination = "Bulgaria";
			if(season.equals("summer")) {
				type = "Camp";
				percent = budget * (30.0f / 100.0f);
				
				System.out.println("Somewhere in " + destination + "\n" +  type + " - " + String.format("%.2f", percent));
			}
			else {
				type = "Hotel";
				percent = budget * (70.0f / 100.0f);
				System.out.println("Somewhere in " + destination + "\n" + type + " - " + String.format("%.2f", percent));
			}
		}
		else if(budget <= 1000 && budget > 100) {
			destination = "Balkans";
			if(season.equals("summer")) {
				type = "Camp";
				percent = budget * (40.0f / 100.0f);
				System.out.println("Somewhere in " + destination + "\n" +  type + " - " + String.format("%.2f", percent));
			}
			else {
				type = "Hotel";
				percent = budget * (80.0f / 100.0f);
				System.out.println("Somewhere in " + destination + "\n" + type + " - " + String.format("%.2f", percent));
			}
		}
		
		else if(budget > 1000) {
			destination = "Europe";
			type = "Hotel";
			percent = budget * (90.0f / 100.0f);
			System.out.println("Somewhere in " + destination + "\n" +  type + " - " + String.format("%.2f", percent));
		}
		scanner.close();
	}

}

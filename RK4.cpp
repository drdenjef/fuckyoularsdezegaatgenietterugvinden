#define _USE_MATH_DEFINES
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
#include <string>
#include <numeric> 
#include <time.h>
#include "3DVectClass.h"
#include "hulpfuncties.h"


/******************************
*							  *
*  Runge-Kutta Method (RK4)	  *
*							  *
******************************/



void RK4(std::vector<double> m, std::vector<Vec> r, std::vector<Vec> v, int N, int iteraties, double h, std::string naam) {

	// maak een file aan waar de posities van de deeltjes wordt bijgehouden
	std::ofstream outfile1(naam + ".txt");
	outfile1 << std::setprecision(15);

	// beginposities meegeven
	for (int j = 0; j < N; j++) {
		outfile1 << r[j].x() << ' ' << r[j].y() << ' ' << r[j].z() << '\t';
	}
	outfile1 << std::endl;

	// maak een file aan waar de energieën worden bijgehouden
	std::ofstream outfile2(naam + "_E.txt");
	outfile2 << std::setprecision(15);

	// maak een file aan waar de relatieve fouten van de energieën worden bijgehouden
	std::ofstream outfile3(naam + "_E_err.txt");
	outfile3 << std::setprecision(15);

	// hou de startenergie van het systeem bij
	double start_energie = Energie(r, v, m);

	std::vector<double> tijd_iteratie;

	// begint te itereren over het aantal iteraties die je wilt uitvoeren
	
	

	for (int i = 0; i < iteraties; i++) {

		clock_t sstart = clock();
		
		double h_var = variabele_h(h, r);
		std::vector<Vec> kv1;
		std::vector<Vec> kv2;
		std::vector<Vec> kv3;
		std::vector<Vec> kr4;
		std::vector<Vec> kv4;

		std::vector<Vec> kr1 = v[j];
		for (int j = 0; j < N; j++) {	
			kv1.push_back(a(m, r, j, N));
		}
		
		std::vector<Vec> kr2 = v[j] + .5*h_var*kv1[j];
		for (int j = 0; j < N; j++) {
			kv2.push_back(a(m, r + .5*h_var*kr1, j, N));
		}

		std::vector<Vec> kr3 = v[j] + .5*h_var*kv2[j];
		for (int j = 0; j < N; j++) {
			kv3.push_back(a(m, r + .5*h_var*kr2, j, N));
		}

		std::vector<Vec> kr4 = v[j] + h_var * kv3[j];
		for (int j = 0; j < N; j++) {	
			kv4.push_back(a(m, r + h_var * kr3, j, N));
		}
		

		r += (h_var / 6) * (kr1 + 2 * kr2 + 2 * kr3 + kr4);
		v += (h_var / 6) * (kv1 + 2 * kv2 + 2 * kv3 + kv4);

		tijd_iteratie.push_back((clock() - sstart) / (CLOCKS_PER_SEC/1000));

		for (int j = 0; j < N; j++) {
			outfile1 << r[j].x() << ' ' << r[j].y() << ' ' << r[j].z() << '\t';
		}
		outfile1 << std::endl;
		outfile2 << Energie(r, v, m) << std::endl;
		outfile3 << error_energie(r, v, m, start_energie) << std::endl;
		
	}

	std::cout << "Posities werden bijgehouden in bestand " << naam << ".txt" << std::endl;
	std::cout << "Energie werd bijgehouden in bestand " << naam << "_E.txt" << std::endl;
	std::cout << "Relatieve energiefouten werden bijgehouden in bestand " << naam << "_E_err.txt" << std::endl;
	outfile1.close();
	outfile2.close();
	outfile3.close();

	double tijd_gemiddelde;
	tijd_gemiddelde = accumulate(tijd_iteratie.begin(), tijd_iteratie.end(), 0.0) / tijd_iteratie.size();

	std::cout << tijd_gemiddelde << ' ' << "milliseconden per iteratie" << std::endl;
}

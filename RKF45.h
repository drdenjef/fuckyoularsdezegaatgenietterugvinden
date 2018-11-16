#ifndef RKF45_H
#define RKF45_H
#define _USE_MATH_DEFINES
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
#include "3DVectClass.h"
#include "hulpfuncties.h"


// functie RKF45 die posities van deeltjes teruggeeft
void RKF45(std::vector<double> m, std::vector<Vec> r, std::vector<Vec> v, int N, int iteraties, double h);


#endif
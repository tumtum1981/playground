

//#include <stdio.h>
//#include <tchar.h>
#include <iostream>

//double g_Stocks[] = { 25,15,10,13,14,16,9,8,7,6,3,8,19,5,6,1 };
//double g_Stocks[] = { 25,15,10,5,10,15,20,25,24,25,15,14,19,21,22,1 };
double g_Stocks[] = { 5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2};
//double g_Stocks[] = { 1,2,3,4,5,5,5,6,6,6,7,7,7,8,8,9};
int NUMBER_OF_STOCKS = 16;


void FindBestProfit( double &a_BestProfit, int &a_Buy, int &a_Sell) {

  // Init profit to first elements, this will be overridden if better found
  a_BestProfit=g_Stocks[1]-g_Stocks[0];                                         
  a_Buy=0;                              // can reove and use l_CurrentBestLow
  a_Sell=1;

  // start at 2 as we already initialised to the first 2 element
  int l_CurrentBestLow=0;
  for (int i=2; i<NUMBER_OF_STOCKS; i++) {

    // 
    if (g_Stocks[i] < g_Stocks[l_CurrentBestLow]) {
      l_CurrentBestLow = i;
    }

    // calc profit using current best low
    if (g_Stocks[i] - g_Stocks[l_CurrentBestLow] > a_BestProfit) {
      // only update best low/high if a better profit is found
      a_Sell = i;
      a_Buy = l_CurrentBestLow;
      a_BestProfit = g_Stocks[i] - g_Stocks[l_CurrentBestLow];
    }
  }

}


int main()//_tmain(int argc, _TCHAR* argv[])
{
  double l_BestProfit = -1;
  int l_Buy = 0;
  int l_Sell = 1;

  FindBestProfit(l_BestProfit, l_Buy, l_Sell);

  // display results
  if (l_BestProfit > 0) {
    //printf("The biggest profit of the day is %.2f\nBuy [%d]\nSell [%d]\n\n"
    //  , l_BestProfit, l_Buy, l_Sell);
    std::cout << "The biggest profit of the day is ";
    std::cout << l_BestProfit;
  } else {
    //printf("No profit was found. Do not buy any stocks, get a cake instead!\n");
    std::cout << "No profit was found. Do not buy any stocks, get a cake instead!\n";
  }

  // wait to complete program
  getchar();

	return 0;
}
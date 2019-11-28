module EulerMaruyama  
    (
        solveBlackScholes
    ) where
  
import RandomHelper

type Steps = Int
type Delta = Double
type Brownian = [Double]

-- Solves for SDE of the form dX_t = a(t, X_t)dt + b(t, X_t)dW_t
-- So for Black Scholes we have aFunc = mu*X_t and bFunc = sigma*X_t
data SDE = SDE { 
    aFunc :: Int -> Double -> Double,
    bFunc :: Int -> Double -> Double
}

-- todo: make this take a sigma and mu
solveBlackScholes :: Steps -> Delta -> [Double] 
solveBlackScholes n d = solve blackScholes n d
        where
            blackScholesFunc1 t x = 0.3*x
            blackScholesFunc2 t x = 0.6*x
            blackScholes = SDE { aFunc = blackScholesFunc1, bFunc = blackScholesFunc2 }

solve :: SDE -> Steps -> Delta -> [Double]
solve eqn n d = solveHelper eqn d 0 (normalSampleList n) []

-- Initial condition: X_0 = 1
-- X_{t+1} = X_t + a(t, X_t)*delta + b(t, X_t)*(i'th brownian) at the i'th step
solveHelper :: SDE -> Delta -> Int -> Brownian -> [Double] -> [Double]
solveHelper eqn d step brownian [] = solveHelper eqn d (step+1) (tail brownian) [1 + aVal*d + bVal*(head brownian)]
        where
            aVal = (aFunc eqn) step 1
            bVal = (aFunc eqn) step 1
solveHelper _ _ _ [] approx = approx
solveHelper eqn d step brownian approx = solveHelper eqn d (step+1) (tail brownian) (approx ++ [currentX + aVal*d + bVal*(head brownian)])
        where
            currentX = last approx
            aVal = (aFunc eqn) step currentX
            bVal = (aFunc eqn) step currentX
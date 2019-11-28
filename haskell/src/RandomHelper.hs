module RandomHelper
    ( 
        normalSampleList
    ) where

import System.Random
import Data.Random.Normal

normalSampleList :: (Random a, Floating a) => Int -> [a]
normalSampleList n = normalSampleHelper n (mkStdGen 0) []

normalSampleHelper :: (Random a, Floating a) => Int -> StdGen -> [a] -> [a]
normalSampleHelper 0 _ result = result
normalSampleHelper n gen result = normalSampleHelper (n-1) newGen (result ++ [sample])
        where (sample, newGen) = normalSample gen

normalSample :: (Random a, Floating a) => StdGen -> (a, StdGen)
normalSample gen = normal gen
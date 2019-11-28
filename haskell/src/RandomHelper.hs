module RandomHelper
    ( 
        normalSampleList
    ) where

import System.Random
import Data.Random.Normal

normalSampleList :: Int -> [Double]
normalSampleList n = normalSampleHelper n (mkStdGen 0) []

normalSampleHelper :: Int -> StdGen -> [Double] -> [Double]
normalSampleHelper 0 _ result = result
normalSampleHelper n gen result = normalSampleHelper (n-1) newGen (result ++ [sample])
        where (sample, newGen) = normalSample gen

normalSample :: StdGen -> (Double, StdGen)
normalSample gen = (sample :: Double, newGen)
    where (sample, newGen) = normal gen
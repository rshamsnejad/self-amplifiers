[Transient Analysis]
{
   Npanes: 1
   {
      traces: 1 {524290,0,"V(out)"}
      Parametric: "V(in)"
      X: (' ',1,-1,0.1,1)
      Y[0]: ('m',0,-0.5,0.1,0.5)
      Y[1]: ('_',0,1e+308,0,-1e+308)
      Volts: ('m',0,0,0,-0.5,0.1,0.5)
      Log: 0 0 0
   }
}

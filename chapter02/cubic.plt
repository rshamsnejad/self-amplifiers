[Transient Analysis]
{
   Npanes: 1
   {
      traces: 1 {524291,0,"V(law_out)"}
      Parametric: "V(law_in)"
      X: (' ',1,-1,0.1,1)
      Y[0]: (' ',1,-1,0.5,1)
      Y[1]: ('_',0,1e+308,0,-1e+308)
      Volts: (' ',0,0,1,-1,0.5,1)
      Log: 0 0 0
   }
}

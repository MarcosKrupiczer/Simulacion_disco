Merge "disco.step";
SetFactory("OpenCASCADE");
BooleanUnion{ Volume{1}; Delete; }{ Volume{2}; Delete; }
//+
Physical Surface("neumann") = {10, 4};
//+
Physical Surface("conveccion") = {9, 8};
//+
Physical Surface("aislado") = {5, 7, 11, 2, 3, 6, 1};
//+
Physical Volume("dominio") = {1};

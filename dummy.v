//Decision Tree
`timescale 1s/1ns
module dummy(x1,x2,x3,x4,x5,rst,out);
input [31:0] x1;
input [31:0] x2;
input [31:0] x3;
input [31:0] x4;
input [31:0] x5;
input rst;
output reg [31:0] out;
reg [31:0] fifty;
reg [31:0] counter;

always  begin

	if (x4<23) begin
		if(x1<9) begin
			class = 0;		
		end
		else begin
			class = 1;
		end
	end
	else if (x4=>23) begin
		class = 1;
	end
				
end

endmodule





sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		if (int(rand(3)) == 0) {
			$dmg1 = $mhp + $whp_flg;
			$sake2 -= 999999;
			$com1 .="<font class=red>急所に狙いを定めた！！</font><br>";
		}
	}
}
sub atowaza{}
1;
sub whissatu{
	if ($wwaza_ritu > int(rand(100))) {
		$com2 .= "<font color=\"$white\">$winner[3]�́A�^���b�g�J�[�h���ꖇ�������I�I ���������H �S�Ă͂��̉^���̃J�[�h�ꖇ�Ɉς˂�ꂽ�b�I�I</font><br>";
		$ura = int(rand(22));
		if (0 == $ura) {
			$com2 .= "THE MAGICIAN�I�I�I�I\n";
			$dmg2 += ($winner[7] + $winner[8]) * int(rand(80));
			$sake1 -= 999999;
		} elsif (1 == $ura) {
			$com2 .= "THE CHARIOT�I�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[10]) * int(rand(80));
			$sake1 -= 999999;
		} elsif (2 == $ura) {
			$com2 .= "STRENGTH�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[9]) * int(rand(80));
			$sake1 -= 999999;
		} elsif (3 == $ura) {
			$com2 .= "THE HIGH PRIESTESS�I�I�I\n";
			$dmg2 = 0;
			$hpplus2 = ($winner[7] + $winner[8]) * int(rand(180));
			$kaihuku2 .= "$winner[3] �̂g�o�� $hpplus2 �񕜂����I��";
		} elsif (4 == $ura) {
			$com2 .= "THE HIEROPHANT�I�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[7] + $winner[8]) * int(rand(80));
			$sake1 -= 999999;
		} elsif (5 == $ura) {
			$com2 .= "THE EMPRESS�I�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[7] + $winner[8]) * int(rand(120));
			$sake1 -= 999999;
		} elsif (6 == $ura) {
			$com2 .= "THE EMPEROR�I�I�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[7] + $winner[8]) * int(rand(180));
			$sake1 -= 999999;
		} elsif (7 == $ura) {
			$com2 .= "THE LOVERS�I�I�I�I\n";
			$dmg2 = 0;
			$hpplus2 = $winner[9] * int(rand(80));
			$kaihuku2 .= "$winner[3] �̂g�o�� $hpplus2 �񕜂����I��";
		} elsif (8 == $ura) {
			$com2 .= "THE HERMIT�I�I�I�I\n";
			$dmg2 += $winner[12] * int(rand(80));
			$sake1 -= 999999;
		} elsif (9 == $ura) {
			$com2 .= "WHEEL of FORTUNE�I�I�I�I\n";
			$dmg2 = ($winner[6] + $winner[7] + $winner[8] + $winner[9] + $winner[10] + $winner[11] + $winner[12]) * int(rand(80));
			$sake1 -= 999999;
		} elsif (10 == $ura) {
			$com2 .= "JUSTICE�I�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[8] ) * int(rand(180));
			$sake1 -= 999999;
		} elsif (11 == $ura) {
			$com2 .= "THE HANGEDMAN�I�I�I�I\n";
			$dmg2 = int(0);
		} elsif (12 == $ura) {
			$com2 .= "DEATH�I�I�I�I\n";
			$dmg2 = $khp_flg + $item[4];
			$sake1 -= 999999;
		} elsif (13 == $ura) {
			$com2 .= "TEMPERANCE�I�I�I�I\n";
			$dmg2 = ($winner[6] + $winner[7] + $winner[8] + $winner[9] + $winner[10] + $winner[11] + $winner[12]) * int(rand(80));	$sake1 -= 999999;
		} elsif (14 == $ura) {
			$com2 .= "THE DEVIL�I�I�I�I\n";
			$dmg2 = 0;
			$dmg1 = $whp_flg;
			$sake2 -= 999999;
		} elsif (15 == $ura) {
			$com2 .= "THE TOWER�I�I�I�I\n";
			$dmg2 = 0;
			$hpplus1 = ($winner[6] + $winner[7] + $winner[8] + $winner[9] + $winner[10] + $winner[11] + $winner[12]) * int(rand(180));
			$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
		} elsif (16 == $ura) {
			$com2 .= "THE STAR�I�I�I�I\n";
			$dmg2 += ($winner[8] + $winner[12]) * int(rand(80));
			$sake1 -= 999999;
		} elsif (17 == $ura) {
			$com2 .= "THE MOON�I�I�I�I\n";
			$dmg2 = 0;
			$hpplus2 = ($winner[7] + $winner[8]) * int(rand(80));
			$kaihuku2 .= "$winner[3] �̂g�o�� $hpplus2 �񕜂����I��";
		} elsif (18 == $ura) {
			$com2 .= "THE SUN�I�I�I�I\n";
			$dmg2 += ($winner[6] + $winner[10]) * int(rand(999));
			$sake1 -= 999999;
		} elsif (19 == $ura) {
			$com2 .= "THE JUDGEMENT�I�I�I�I\n";
			$dmg2 += ($winner[7] + $winner[8]) * int(rand(999));
			$sake1 -= 999999;
		} elsif (20 == $ura) {
			$com2 .= "THE WORLD�I�I�I�I\n";
			$dmg2 = ($winner[6] + $winner[7] + $winner[8] + $winner[9] + $winner[10] + $winner[11] + $winner[12]) * int(rand(80));
			$sake1 -= 999999;
		} else {
			$com2 .= "THE FOOL\n";
			$dmg2 = int(1);
		}
	}
}
sub watowaza{}
1;
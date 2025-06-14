//package br.ufba.jnose.pages.charts;
//
//import de.adesso.wickedcharts.highcharts.options.*;
//import de.adesso.wickedcharts.highcharts.options.color.HexColor;
//import de.adesso.wickedcharts.highcharts.options.series.SimpleSeries;
//
//import java.util.ArrayList;
//import java.util.List;
//
//public class UserCommitBarOptions extends Options {
//
//    private static final long serialVersionUID = 1L;
//
//    public UserCommitBarOptions(List<List<String>> todasLinhas) {
//
//
//        List<String> listNames = new ArrayList<>();
//        List<Number> listCont = new ArrayList<>();
//
//        for(List<String> linha : todasLinhas){
//            listNames.add(linha.get(0));
//            listCont.add(Integer.parseInt(linha.get(1)));
//        }
//
//        setChartOptions(new ChartOptions()
//                .setType(SeriesType.BAR));
//
//        setGlobal(new Global()
//                .setUseUTC(Boolean.TRUE));
//
//        setTitle(new Title("TestSmells by User and Commit"));
//
//        setSubtitle(new Title("Source: JNose"));
//
//        setxAxis(new Axis()
//                .setCategories(listNames)
//                .setTitle(new Title(null)));
//
//        setyAxis(new Axis()
//                .setTitle(
//                        new Title("TestSmells")
//                                .setAlign(HorizontalAlignment.HIGH))
//                .setLabels(new Labels().setOverflow(Overflow.JUSTIFY)));
//
//        setTooltip(new Tooltip()
//                .setFormatter(new Function(
//                        "return ''+this.series.name +': '+ this.y +'';")));
//
//        setPlotOptions(new PlotOptionsChoice()
//                .setBar(new PlotOptions()
//                        .setDataLabels(new DataLabels()
//                                .setEnabled(Boolean.TRUE))));
//
//        setLegend(new Legend()
//                .setLayout(LegendLayout.VERTICAL)
//                .setAlign(HorizontalAlignment.RIGHT)
//                .setVerticalAlign(VerticalAlignment.TOP)
//                .setX(-100)
//                .setY(100)
//                .setFloating(Boolean.TRUE)
//                .setBorderWidth(1)
//                .setBackgroundColor(new HexColor("#ffffff"))
//                .setShadow(Boolean.TRUE));
//
//        setCredits(new CreditOptions()
//                .setEnabled(Boolean.FALSE));
//
//        addSeries(new SimpleSeries()
//                .setName("TestSmells")
//                .setData(listCont));
//
//
//    }
//
//    public String getLabel() {
//        return "Basic bar";
//    }
//
//}

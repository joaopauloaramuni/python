//package br.ufba.jnose.pages.charts;
//
//import java.text.ParseException;
//import java.text.SimpleDateFormat;
//import java.util.*;
//
//import de.adesso.wickedcharts.highcharts.options.*;
//import de.adesso.wickedcharts.highcharts.options.color.HexColor;
//import de.adesso.wickedcharts.highcharts.options.series.Series;
//import de.adesso.wickedcharts.highcharts.options.series.SimpleSeries;
//import org.apache.commons.lang3.ArrayUtils;
//
//public class BasicLineOptions extends Options {
//    private static final long serialVersionUID = 1L;
//
//    public BasicLineOptions(List<List<String>> todasLinhas) {
//
//        String[] listaDatas = new String[todasLinhas.size()];
//        Number[] listaValores = new Number[todasLinhas.size()];
//
//        Date testeDate = new Date();
//
//        SimpleDateFormat fd = new SimpleDateFormat("EEE MMM dd HH:mm:ss zzz yyyy", Locale.US);
//        SimpleDateFormat fd2 = new SimpleDateFormat("dd-MM-yyyy", Locale.US);
////        Wed Nov 26 10:20:37 BRT 2014
//
//        System.out.println(fd.format(testeDate));
//
//        int cont = 0;
//        for (List<String> lista : todasLinhas) {
//            System.out.println(lista);
//            try {
//                Date data = fd.parse(lista.get(2));
//                listaDatas[cont] = fd2.format(data);
//            } catch (ParseException e) {
//                e.printStackTrace();
//            }
//            listaValores[cont] = Integer.parseInt(lista.get(3));
//            cont++;
//        }
//
//        ArrayUtils.reverse(listaDatas);
//        ArrayUtils.reverse(listaValores);
//
//
//        ChartOptions chartOptions = new ChartOptions();
//        chartOptions.setType(SeriesType.LINE);
//        chartOptions.setMarginRight(130);
//        chartOptions.setMarginBottom(100);
//        setChartOptions(chartOptions);
//
//        Title title = new Title("Total de TestSmells by Commit");
//        title.setX(-20);
//        setTitle(title);
//
//        Title subTitle = new Title("Source: JNose");
//        subTitle.setX(-20);
//        setSubtitle(subTitle);
//
//        Axis xAxis = new Axis();
//        xAxis.setCategories(Arrays.asList(listaDatas));
//        setxAxis(xAxis);
//
//        PlotLine plotLines = new PlotLine();
//        plotLines.setValue(0f);
//        plotLines.setWidth(1);
//        plotLines.setColor(new HexColor("#999999"));
//
//        Axis yAxis = new Axis();
//        yAxis.setTitle(new Title("Total of TestSmells"));
//        yAxis.setPlotLines(Collections.singletonList(plotLines));
//        setyAxis(yAxis);
//
//        Legend legend = new Legend();
//        legend.setLayout(LegendLayout.VERTICAL);
//        legend.setAlign(HorizontalAlignment.RIGHT);
//        legend.setVerticalAlign(VerticalAlignment.TOP);
//        legend.setX(-10);
//        legend.setY(100);
//        legend.setBorderWidth(0);
//        setLegend(legend);
//
//        Series<Number> series1 = new SimpleSeries();
//        series1.setName("");
//        series1.setShowInLegend(false);
//        series1.setData(Arrays.asList(listaValores));
//        addSeries(series1);
//    }
//}
